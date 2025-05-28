module.exports = {
  content: ["./templates/**/*.html", "./pages/**/*.md"],
  darkMode: "media",
  theme: {
    container: {
      padding: "2rem",
      center: true,
      screens: {
        sm: "500px",
        md: "600px",
        lg: "800px",
        xl: "1000px",
        "2xl": "1200px",
      },
    },
    extend: {
      fontFamily: {
        sans: ["--apple-system", "system-ui", "sans-serif", "ui-sans-serif"],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: "75ch",
          },
        },
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
