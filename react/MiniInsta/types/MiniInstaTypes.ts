// File: MiniInstaTypes.ts
// Author: Jordan Yin (jordany@bu.edu), 11/19/2026
// Description: Shared data types and constants used throughout MiniInsta.

export type Profile = {
  id: number;
  username: string;
  display_name: string;
  profile_image_url: string;
  bio_text: string;
  post_count: number;
};

export type Photo = {
  id: number;
  image: string;
};

export type Post = {
  id: number;
  profile_id: number;
  caption: string;
  timestamp: string;
  photos: Photo[];
};

export const API_BASE_URL = 'https://cs-webapps.bu.edu/jordany';
export const PROFILE_ID = 3;
export const FALLBACK_IMAGE =
  'https://img.magnific.com/premium-vector/letter-x-dry-brush-stroke-typography-vector_53876-177859.jpg';
