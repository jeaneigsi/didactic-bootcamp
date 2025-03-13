export interface User {
  id: number;
  email: string;
  username: string;
  first_name?: string;
  last_name?: string;
}

export interface Parcelle {
  id: number;
  nom: string;
  prix: number;
  categorie: string;
  ville: string;
  description: string;
  image: string;
  superficie: number;
  created_at: string;
  isFavorite?: boolean;
}

export interface AuthResponse {
  token: string;
}

export interface PredictionResult {
  score: string;
  message: string;
}

export interface SearchFilters {
  ville?: string;
  categorie?: string;
  minPrix?: number;
  maxPrix?: number;
  minSuperficie?: number;
  maxSuperficie?: number;
}