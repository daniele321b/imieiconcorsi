/** Variabile d'ambiente obbligatoria (le passa Terraform a ogni Lambda). */
export function env(nome: string) {
  const valore = process.env[nome];
  if (!valore) throw new Error(`Variabile d'ambiente ${nome} mancante`);
  return valore;
}
