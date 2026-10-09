import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// In locale /api (e la lista dei bandi in cache, /dati) vanno al CloudFront dell'ambiente su AWS
// (scripts/deploy.sh local imposta API_PROXY_TARGET), così gli indirizzi sono gli stessi della produzione.
const apiTarget = process.env.API_PROXY_TARGET;

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 5173,
    strictPort: true,
    proxy: apiTarget
      ? {
          "/api": { target: apiTarget, changeOrigin: true, secure: true },
          "/dati": { target: apiTarget, changeOrigin: true, secure: true },
        }
      : undefined,
  },
});
