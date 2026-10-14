// Font servito dal nostro sito (non da Google Fonts): niente IP dei visitatori a terzi e una
// Content-Security-Policy più stretta (modules/web, font-src 'self').
import "@fontsource-variable/plus-jakarta-sans";
import "./index.css";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, Navigate, Outlet, RouterProvider, ScrollRestoration } from "react-router";
import { AuthProvider } from "./lib/auth";
import { caricaConfig } from "./lib/config";
import { ricordaInvito } from "./lib/invito";
import { ricordaProvenienza } from "./lib/provenienza";
import { Admin } from "./pages/app/Admin";
import { AdminBancheDati } from "./pages/app/AdminBancheDati";
import { AdminPagamenti } from "./pages/app/AdminPagamenti";
import { AdminRichieste } from "./pages/app/AdminRichieste";
import { Assistenza } from "./pages/app/Assistenza";
import { BancaDatiConsulta } from "./pages/app/BancaDatiConsulta";
import { BancheDati } from "./pages/app/BancheDati";
import { AppLayout } from "./pages/app/AppLayout";
import { Concorsi } from "./pages/app/Concorsi";
import { ConcorsoDettaglio } from "./pages/app/ConcorsoDettaglio";
import { Dashboard } from "./pages/app/Dashboard";
import { Onboarding } from "./pages/app/Onboarding";
import { Pagamento } from "./pages/app/Pagamento";
import { Piani } from "./pages/app/Piani";
import { Profilo } from "./pages/app/Profilo";
import { SessionePage } from "./pages/app/Sessione";
import { Studio } from "./pages/app/Studio";
import { Tutor } from "./pages/app/Tutor";
import { AuthCallback } from "./pages/AuthCallback";
import { Disiscrivi } from "./pages/Disiscrivi";
import { EliminazioneDati } from "./pages/legale/EliminazioneDati";
import { Privacy } from "./pages/legale/Privacy";
import { Termini } from "./pages/legale/Termini";
import { Errore } from "./pages/Errore";
import { ChiSiamo } from "./pages/info/ChiSiamo";
import { Contatti } from "./pages/info/Contatti";
import { Cookie } from "./pages/info/Cookie";
import { DomandeFrequenti } from "./pages/info/DomandeFrequenti";
import { LeNostreEmail } from "./pages/info/LeNostreEmail";
import { Prezzi } from "./pages/info/Prezzi";
import { Landing } from "./pages/Landing";

// Punto di partenza del sito: legge la configurazione (config.json), avvia il login (AuthProvider)
// e definisce le pagine. Le pagine pubbliche stanno sotto "/", l'area riservata sotto "/app"
// (AppLayout: menu, controllo del login e dell'onboarding) e il pannello di controllo sotto "/admin".

/** Indirizzo → pagina. */
const router = createBrowserRouter([
  {
    // Radice di tutte le pagine: ogni pagina nuova si apre dall'alto (sul telefono restava a metà),
    // tornando indietro si ritrova il punto dov'eri.
    element: <Radice />,
    errorElement: <Errore />,
    children: [
  { path: "/", element: <Landing />, errorElement: <Errore /> },
  { path: "/auth/callback", element: <AuthCallback /> },
  // Pagine legali pubbliche (anche per Meta e Google: privacy ed eliminazione dati).
  { path: "/privacy", element: <Privacy /> },
  { path: "/termini", element: <Termini /> },
  { path: "/eliminazione-dati", element: <EliminazioneDati /> },
  { path: "/disiscrivi", element: <Disiscrivi /> },
  // Pagine pubbliche informative (piè di pagina e home).
  { path: "/chi-siamo", element: <ChiSiamo /> },
  { path: "/prezzi", element: <Prezzi /> },
  { path: "/domande-frequenti", element: <DomandeFrequenti /> },
  { path: "/contatti", element: <Contatti /> },
  { path: "/email", element: <LeNostreEmail /> },
  { path: "/cookie", element: <Cookie /> },
  {
    path: "/app",
    element: <AppLayout />,
    // Una pagina che va in errore mostra un messaggio comprensibile, non la schermata tecnica.
    errorElement: <Errore />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "onboarding", element: <Onboarding /> },
      { path: "concorsi", element: <Concorsi /> },
      { path: "concorsi/:id", element: <ConcorsoDettaglio /> },
      { path: "studio", element: <Studio /> },
      { path: "banche-dati", element: <BancheDati /> },
      { path: "banche-dati/:id", element: <BancaDatiConsulta /> },
      { path: "tutor", element: <Tutor /> },
      { path: "sessione/:id", element: <SessionePage /> },
      { path: "piani", element: <Piani /> },
      { path: "pagamento", element: <Pagamento /> },
      { path: "profilo", element: <Profilo /> },
      { path: "assistenza", element: <Assistenza /> },
    ],
  },
  {
    // Pannello di controllo: solo gruppo Cognito "admin" (lo ricontrolla anche il backend).
    path: "/admin",
    element: <AppLayout />,
    errorElement: <Errore />,
    children: [
      { index: true, element: <Admin /> },
      { path: "banche-dati", element: <AdminBancheDati /> },
      { path: "pagamenti", element: <AdminPagamenti /> },
      { path: "richieste", element: <AdminRichieste /> },
    ],
  },
  { path: "*", element: <Navigate to="/" replace /> },
],
  },
]);

/** Ripristino dello scorrimento + la pagina corrente. */
function Radice() {
  return (
    <>
      <ScrollRestoration />
      <Outlet />
    </>
  );
}

const root = createRoot(document.getElementById("root")!);
// Arrivati da un link "invita un amico" o da un link dei social con i parametri UTM:
// codice e provenienza servono dopo la registrazione.
ricordaInvito();
ricordaProvenienza();

caricaConfig()
  .then(() =>
    root.render(
      <StrictMode>
        <AuthProvider>
          <RouterProvider router={router} />
        </AuthProvider>
      </StrictMode>,
    ),
  )
  .catch((err) => {
    console.error(err);
    root.render(
      <p style={{ padding: 24, fontFamily: "sans-serif" }}>
        Configurazione dell'app non trovata. In locale esegui <code>npm run dev</code> dalla radice del progetto.
      </p>,
    );
  });
