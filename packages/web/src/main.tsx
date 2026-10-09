import "./index.css";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router";
import { AuthProvider } from "./lib/auth";
import { caricaConfig } from "./lib/config";
import { Admin } from "./pages/app/Admin";
import { AdminBancheDati } from "./pages/app/AdminBancheDati";
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
import { AuthCallback } from "./pages/AuthCallback";
import { Disiscrivi } from "./pages/Disiscrivi";
import { EliminazioneDati } from "./pages/legale/EliminazioneDati";
import { Privacy } from "./pages/legale/Privacy";
import { Termini } from "./pages/legale/Termini";
import { Landing } from "./pages/Landing";

const router = createBrowserRouter([
  { path: "/", element: <Landing /> },
  { path: "/auth/callback", element: <AuthCallback /> },
  // Pagine legali pubbliche (anche per Meta e Google: privacy ed eliminazione dati).
  { path: "/privacy", element: <Privacy /> },
  { path: "/termini", element: <Termini /> },
  { path: "/eliminazione-dati", element: <EliminazioneDati /> },
  { path: "/disiscrivi", element: <Disiscrivi /> },
  {
    path: "/app",
    element: <AppLayout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "onboarding", element: <Onboarding /> },
      { path: "concorsi", element: <Concorsi /> },
      { path: "concorsi/:id", element: <ConcorsoDettaglio /> },
      { path: "studio", element: <Studio /> },
      { path: "banche-dati", element: <BancheDati /> },
      { path: "sessione/:id", element: <SessionePage /> },
      { path: "piani", element: <Piani /> },
      { path: "pagamento", element: <Pagamento /> },
      { path: "profilo", element: <Profilo /> },
    ],
  },
  {
    // Pannello di controllo: solo gruppo Cognito "admin" (lo ricontrolla anche il backend).
    path: "/admin",
    element: <AppLayout />,
    children: [
      { index: true, element: <Admin /> },
      { path: "banche-dati", element: <AdminBancheDati /> },
    ],
  },
  { path: "*", element: <Navigate to="/" replace /> },
]);

const root = createRoot(document.getElementById("root")!);

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
