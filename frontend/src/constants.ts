const envFile = import.meta.env as EnvVariables;

interface EnvVariables {
  VITE_BASE_URL?: string;
}

export const DEFAULT_PRICE_DECIMAL_PLACES = 2;

// export const BASE_URL = envFile.VITE_BASE_URL || "api/";
export const BASE_URL = "http://localhost:8000/";
