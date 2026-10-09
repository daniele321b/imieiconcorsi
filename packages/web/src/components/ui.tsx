import { AlertTriangle, CheckCircle2, Info, Loader2, Sparkles, X } from "lucide-react";
import { useEffect, type ButtonHTMLAttributes, type InputHTMLAttributes, type ReactNode } from "react";
import { Link } from "react-router";

export const cx = (...c: (string | false | null | undefined)[]) => c.filter(Boolean).join(" ");

type Variant = "primary" | "secondary" | "ghost" | "danger" | "accent";

const VARIANTI: Record<Variant, string> = {
  primary: "bg-brand-600 text-white hover:bg-brand-700 shadow-sm shadow-brand-600/30",
  accent: "bg-accent-400 text-brand-950 hover:bg-accent-300 shadow-sm shadow-accent-500/30",
  secondary: "bg-white text-slate-800 ring-1 ring-slate-200 hover:bg-slate-50 hover:ring-slate-300",
  ghost: "text-slate-600 hover:bg-slate-100 hover:text-slate-900",
  danger: "bg-rose-600 text-white hover:bg-rose-700",
};

const SIZES = {
  sm: "h-8 px-3 text-sm gap-1.5 rounded-lg",
  md: "h-10 px-4 text-sm gap-2 rounded-xl",
  lg: "h-12 px-6 text-base gap-2 rounded-xl",
};

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  size?: keyof typeof SIZES;
  loading?: boolean;
}

export function Button({ variant = "primary", size = "md", loading, className, children, disabled, ...props }: ButtonProps) {
  return (
    <button
      className={cx(
        "inline-flex items-center justify-center font-semibold transition disabled:cursor-not-allowed disabled:opacity-60",
        VARIANTI[variant],
        SIZES[size],
        className,
      )}
      disabled={disabled || loading}
      {...props}
    >
      {loading && <Loader2 className="size-4 animate-spin" />}
      {children}
    </button>
  );
}

export function ButtonLink({
  to,
  variant = "primary",
  size = "md",
  className,
  children,
}: {
  to: string;
  variant?: Variant;
  size?: keyof typeof SIZES;
  className?: string;
  children: ReactNode;
}) {
  return (
    <Link
      to={to}
      className={cx("inline-flex items-center justify-center font-semibold transition", VARIANTI[variant], SIZES[size], className)}
    >
      {children}
    </Link>
  );
}

export function Card({ className, children }: { className?: string; children: ReactNode }) {
  return <div className={cx("rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200/70", className)}>{children}</div>;
}

const BADGE = {
  slate: "bg-slate-100 text-slate-700",
  brand: "bg-brand-50 text-brand-700 ring-1 ring-brand-100",
  green: "bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100",
  red: "bg-rose-50 text-rose-700 ring-1 ring-rose-100",
  amber: "bg-amber-50 text-amber-800 ring-1 ring-amber-100",
};

export function Badge({ tone = "slate", className, children }: { tone?: keyof typeof BADGE; className?: string; children: ReactNode }) {
  return (
    <span className={cx("inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-xs font-semibold", BADGE[tone], className)}>
      {children}
    </span>
  );
}

interface FieldProps extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  hint?: string;
}

export function Field({ label, hint, id, className, ...props }: FieldProps) {
  const inputId = id ?? props.name;
  return (
    <label htmlFor={inputId} className={cx("block", className)}>
      <span className="mb-1.5 block text-sm font-medium text-slate-700">{label}</span>
      <input
        id={inputId}
        className="block h-11 w-full rounded-xl border-0 bg-white px-3.5 text-slate-900 ring-1 ring-slate-300 transition placeholder:text-slate-400 focus:ring-2 focus:ring-brand-500 focus:outline-none"
        {...props}
      />
      {hint && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
    </label>
  );
}

const ALERT = {
  error: { cls: "bg-rose-50 text-rose-800 ring-rose-200", Icon: AlertTriangle },
  success: { cls: "bg-emerald-50 text-emerald-800 ring-emerald-200", Icon: CheckCircle2 },
  info: { cls: "bg-brand-50 text-brand-900 ring-brand-200", Icon: Info },
};

export function Alert({ tone = "info", children, onClose }: { tone?: keyof typeof ALERT; children: ReactNode; onClose?: () => void }) {
  const { cls, Icon } = ALERT[tone];
  return (
    <div role={tone === "error" ? "alert" : "status"} className={cx("flex gap-3 rounded-xl p-3.5 text-sm ring-1", cls)}>
      <Icon className="mt-0.5 size-4 shrink-0" />
      <div className="flex-1">{children}</div>
      {onClose && (
        <button onClick={onClose} aria-label="Chiudi" className="opacity-60 hover:opacity-100">
          <X className="size-4" />
        </button>
      )}
    </div>
  );
}

export function Spinner({ label = "Caricamento…" }: { label?: string }) {
  return (
    <div className="flex items-center justify-center gap-2 py-16 text-slate-500">
      <Loader2 className="size-5 animate-spin" />
      <span className="text-sm">{label}</span>
    </div>
  );
}

export function FullPageSpinner() {
  return (
    <div className="grid min-h-screen place-items-center">
      <Spinner />
    </div>
  );
}

export function ProgressBar({ value, tone = "brand", className }: { value: number; tone?: "brand" | "green" | "amber" | "red"; className?: string }) {
  const colori = { brand: "bg-brand-500", green: "bg-emerald-500", amber: "bg-amber-400", red: "bg-rose-500" };
  return (
    <div className={cx("h-2 overflow-hidden rounded-full bg-slate-100", className)}>
      <div className={cx("h-full rounded-full transition-all duration-500", colori[tone])} style={{ width: `${Math.min(100, Math.max(0, value))}%` }} />
    </div>
  );
}

export function EmptyState({ icon, title, children, action }: { icon: ReactNode; title: string; children?: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex flex-col items-center rounded-2xl border-2 border-dashed border-slate-200 px-6 py-10 text-center">
      <div className="mb-3 grid size-12 place-items-center rounded-2xl bg-brand-50 text-brand-600">{icon}</div>
      <h3 className="font-semibold text-slate-900">{title}</h3>
      {children && <p className="mt-1 max-w-sm text-sm text-slate-500">{children}</p>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  );
}

export function PageHeader({ title, subtitle, actions }: { title: string; subtitle?: ReactNode; actions?: ReactNode }) {
  return (
    <div className="mb-6 flex flex-wrap items-end justify-between gap-4">
      <div>
        <h1 className="text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl">{title}</h1>
        {subtitle && <p className="mt-1 text-slate-500">{subtitle}</p>}
      </div>
      {actions}
    </div>
  );
}

/** Mostrato quando il server risponde LIMITE_PIANO. */
export function UpgradeBanner({ message, onClose }: { message: string; onClose?: () => void }) {
  return (
    <div className="flex flex-wrap items-center gap-3 rounded-2xl bg-gradient-to-r from-brand-700 to-brand-500 p-4 text-white shadow-lg shadow-brand-600/20">
      <Sparkles className="size-5 shrink-0 text-accent-300" />
      <p className="flex-1 text-sm font-medium">{message}</p>
      <ButtonLink to="/app/piani" variant="accent" size="sm">
        Vedi i piani
      </ButtonLink>
      {onClose && (
        <button onClick={onClose} aria-label="Chiudi" className="text-white/70 hover:text-white">
          <X className="size-4" />
        </button>
      )}
    </div>
  );
}

/** Popup "funzione dei piani a pagamento": si chiude con la X, con Esc o cliccando fuori. */
export function PremiumModal({ titolo, children, onClose }: { titolo: string; children: ReactNode; onClose: () => void }) {
  useEffect(() => {
    const esc = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", esc);
    return () => window.removeEventListener("keydown", esc);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 grid place-items-center bg-slate-950/50 p-4 backdrop-blur-sm" onClick={onClose}>
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby="premium-titolo"
        onClick={(e) => e.stopPropagation()}
        className="w-full max-w-md animate-fade-up rounded-3xl bg-white p-6 shadow-2xl sm:p-8"
      >
        <div className="flex items-start justify-between gap-4">
          <span className="grid size-11 place-items-center rounded-2xl bg-brand-950">
            <Sparkles className="size-5 text-accent-300" />
          </span>
          <button onClick={onClose} aria-label="Chiudi" className="text-slate-400 hover:text-slate-700">
            <X className="size-5" />
          </button>
        </div>
        <h2 id="premium-titolo" className="mt-4 text-xl font-extrabold text-slate-900">
          {titolo}
        </h2>
        <div className="mt-2 text-sm text-slate-600">{children}</div>
        <div className="mt-6 flex flex-wrap justify-end gap-2">
          <Button variant="ghost" onClick={onClose}>
            Non ora
          </Button>
          <ButtonLink to="/app/piani" variant="accent">
            Vedi i piani
          </ButtonLink>
        </div>
      </div>
    </div>
  );
}
