import type { APIRoute } from "astro";
import articles from "../../build/articles.json" assert { type: "json" };
import placeholders from "../../build/placeholders.json" assert { type: "json" };

const PLACEHOLDER_SLUGS = new Set(Object.keys(placeholders || {}));

export const GET: APIRoute = async ({ site }) => {
  const base = site ? site.toString().replace(/\/$/, "") : "";
  const urls = articles
    .map((article: { slug: string; type: string }) => article.slug)
    .filter((slug) => slug && !PLACEHOLDER_SLUGS.has(slug));

  const entries = urls
    .map((slug) => `<url><loc>${base}/wiki/${slug}/</loc></url>`)
    .join("");

  const body =
    `<?xml version="1.0" encoding="UTF-8"?>` +
    `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">` +
    `<url><loc>${base}/</loc></url>` +
    entries +
    `</urlset>`;

  return new Response(body, {
    status: 200,
    headers: {
      "Content-Type": "application/xml",
    },
  });
};
