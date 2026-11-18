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
  caption: string;
  timestamp: string;
  photos: Photo[];
};
