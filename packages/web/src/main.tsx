import "./index.css";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router";
import { AuthProvider } from "./lib/auth";
import { caricaConfig } from "./lib/config";
import { Admin } from "./pages/app/Admin";
import { AppLayout } from "./pages/app/AppLayout";
import { Concorsi } from "./pages/app/Concorsi";
import { ConcorsoDettaglio } from "./pages/app/ConcorsoDettaglio";
import { Dashboard } from "./pages/app/Dashboard";
import { Onboarding } from "./pages/app/Onboarding";
import { Piani } from "./pages/app/Piani";
import { Profilo } from "./pages/app/Profilo";
import { SessionePage } from "./pages/app/Sessione";
import { Studio } from "./pages/app/Studio";
import { AuthCallback } from "./pages/AuthCallback";
import { Landing } from "./pages/Landing";

const router = createBrowserRouter([
  { path: "/", element: <Landing /> },
  { path: "/auth/callback", element: <AuthCallback /> },
  {
    path: "/app",
    element: <AppLayout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "onboarding", element: <Onboarding /> },
      { path: "concorsi", element: <Concorsi /> },
      { path: "concorsi/:id", element: <ConcorsoDettaglio /> },
      { path: "studio", element: <Studio /> },
      { path: "sessione/:id", element: <SessionePage /> },
      { path: "piani", element: <Piani /> },
      { path: "profilo", element: <Profilo /> },
    ],
  },
  {
    // Pannello di controllo: solo gruppo Cognito "admin" (lo ricontrolla anche il backend).
    path: "/admin",
    element: <AppLayout />,
    children: [{ index: true, element: <Admin /> }],
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
