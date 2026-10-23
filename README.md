# iMieiConcorsi

Web app per prepararsi ai concorsi pubblici: bandi da inPA, studio per materia e
simulazioni d'esame. Il piano di prodotto è nel documento "App Concorsi — Piano MVP in 8 settimane".

- **Infrastruttura:** Terraform, in `infra/terraform`. Per ora c'è solo l'ambiente `dev`.
- **Applicazione:** TypeScript. Le Lambda sono in `packages/functions` e il sito React in `packages/web`.
- **Comandi:** sono tutti in `scripts/deploy.sh`.

```bash
export AWS_PROFILE=<il-tuo-profilo>
scripts/deploy.sh bootstrap   # una volta sola
scripts/deploy.sh all
```

- [docs/COMANDI-RAPIDI.md](docs/COMANDI-RAPIDI.md): i comandi pronti da copiare
- [docs/DEPLOY.md](docs/DEPLOY.md): architettura e runbook
- [docs/MANUTENZIONE.md](docs/MANUTENZIONE.md): chiudere il sito con la pagina di manutenzione quando c'è un problema
- [docs/TEST-DI-CARICO.md](docs/TEST-DI-CARICO.md): ambiente preprod e test di carico con k6 (1.000 utenti contemporanei)
- [docs/ARCHITETTURA.md](docs/ARCHITETTURA.md): guida per sviluppatori (flussi, dati, come aggiungere route, tabelle, job, pagine)
- [docs/MAPPA-CODICE.md](docs/MAPPA-CODICE.md): cosa fa ogni file, componente e modulo Terraform
