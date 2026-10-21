import { describe, expect, it } from "vitest";
import { dividiMessaggio, motivoScarto, nomeEIndirizzo, preparaInoltro } from "../src/posta/logic";

// Inoltro della posta di info@ / info-dev@ all'admin (packages/functions/src/posta): il mittente
// diventa il nostro indirizzo, "Rispondi" va al mittente vero, corpo e allegati restano identici.

/** Un messaggio come lo salva SES (righe CRLF), con firma DKIM e intestazione ripiegata. */
const MESSAGGIO = [
  "Return-Path: <mario@gmail.com>",
  "DKIM-Signature: v=1; a=rsa-sha256; d=gmail.com;",
  "\tb=abc123",
  "From: Mario Rossi <mario@gmail.com>",
  "To: info@imieiconcorsi.it",
  "Subject: Domanda sulla banca dati",
  "Message-ID: <x1@mail.gmail.com>",
  "Content-Type: text/plain; charset=UTF-8",
  "",
  "Buongiorno,",
  "quando caricate la banca dati?",
  "",
].join("\r\n");

describe("inoltro della posta in arrivo", () => {
  it("divide intestazioni (righe ripiegate riunite) e corpo", () => {
    const { intestazioni, corpo } = dividiMessaggio(MESSAGGIO);
    expect(intestazioni.find((h) => h.nome === "DKIM-Signature")!.valore).toBe("v=1; a=rsa-sha256; d=gmail.com;\r\n\tb=abc123");
    expect(corpo).toBe("Buongiorno,\r\nquando caricate la banca dati?\r\n");
  });

  it("mittente riscritto sul nostro indirizzo, risposta al mittente vero, firme tolte, corpo identico", () => {
    const fuori = preparaInoltro(MESSAGGIO, "info@imieiconcorsi.it");
    const { intestazioni, corpo } = dividiMessaggio(fuori);
    const valore = (n: string) => intestazioni.filter((h) => h.nome.toLowerCase() === n.toLowerCase()).map((h) => h.valore);
    expect(valore("From")).toEqual(['"Mario Rossi tramite iMieiConcorsi" <info@imieiconcorsi.it>']);
    expect(valore("Reply-To")).toEqual(["mario@gmail.com"]);
    expect(valore("To")).toEqual(["info@imieiconcorsi.it"]);
    expect(valore("Subject")).toEqual(["Domanda sulla banca dati"]);
    for (const via of ["DKIM-Signature", "Return-Path", "Message-ID"]) expect(valore(via)).toEqual([]);
    expect(corpo).toBe("Buongiorno,\r\nquando caricate la banca dati?\r\n");
  });

  it("tiene il Reply-To del mittente, se ne aveva uno", () => {
    const conRisposta = MESSAGGIO.replace("To: info@", "Reply-To: segreteria@ente.it\r\nTo: info@");
    expect(preparaInoltro(conRisposta, "info@imieiconcorsi.it")).toContain("\r\nReply-To: segreteria@ente.it\r\n");
  });

  it("nome con accenti: codificato per l'intestazione (byte UTF-8 del messaggio originale)", () => {
    // Il messaggio si tratta come byte grezzi: "Niccolò" in UTF-8 letto come latin1.
    const grezzo = Buffer.from(MESSAGGIO.replace("Mario Rossi", "Niccolò Bianchi"), "utf8").toString("latin1");
    const from = dividiMessaggio(preparaInoltro(grezzo, "info@imieiconcorsi.it")).intestazioni.find((h) => h.nome === "From")!.valore;
    const codificato = from.match(/^=\?UTF-8\?B\?([^?]+)\?= <info@imieiconcorsi\.it>$/)![1]!;
    expect(Buffer.from(codificato, "base64").toString("utf8")).toBe("Niccolò Bianchi tramite iMieiConcorsi");
  });

  it("legge nome e indirizzo nei formati comuni", () => {
    expect(nomeEIndirizzo('"Rossi, Mario" <mario@gmail.com>')).toEqual({ nome: "Rossi, Mario", indirizzo: "mario@gmail.com" });
    expect(nomeEIndirizzo("mario@gmail.com")).toEqual({ nome: "", indirizzo: "mario@gmail.com" });
  });

  it("scarta virus e spam secondo SES; il resto si inoltra", () => {
    expect(motivoScarto({ virus: "FAIL", spam: "PASS" })).toBe("virus");
    expect(motivoScarto({ virus: "PASS", spam: "FAIL" })).toBe("spam");
    expect(motivoScarto({ virus: "PASS", spam: "GRAY" })).toBeUndefined();
    expect(motivoScarto({ virus: "PROCESSING_FAILED" })).toBeUndefined();
  });
});
