/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./components/**/*.{vue,js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{vue,js,ts,jsx,tsx,mdx}",
    "./layouts/**/*.{vue,js,ts,jsx,tsx,mdx}",
    "./App.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

