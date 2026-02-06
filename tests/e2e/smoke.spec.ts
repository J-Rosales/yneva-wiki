import { expect, test } from "@playwright/test";

test("home page renders", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveTitle(/Yneva Wiki/i);
  await expect(page.locator("a.site-header__brand")).toHaveText("Yneva Wiki");
});

test("search page renders", async ({ page }) => {
  await page.goto("/search/");
  await expect(page.getByRole("heading", { name: "Search" })).toBeVisible();
  await expect(page.locator("#query")).toBeVisible();
});

test("wiki article page renders", async ({ page }) => {
  await page.goto("/wiki/justinian-i/");
  await expect(page.getByRole("heading", { level: 1, name: "Justinian I" })).toBeVisible();
  await expect(page.locator(".wiki__content")).toBeVisible();
});
