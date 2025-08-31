# This script creates a complete React + Vite multi-page portfolio project for Avichal Baweja,
# with Tailwind CSS and Framer Motion, and zips it for download.

import os, json, textwrap, zipfile, pathlib

project_root = "/mnt/data/avichal-portfolio-react"
src_dir = os.path.join(project_root, "src")
pages_dir = os.path.join(src_dir, "pages")
components_dir = os.path.join(src_dir, "components")
public_dir = os.path.join(project_root, "public")

os.makedirs(pages_dir, exist_ok=True)
os.makedirs(components_dir, exist_ok=True)
os.makedirs(public_dir, exist_ok=True)

# ---------------------- package.json ----------------------
package_json = {
  "name": "avichal-portfolio",
  "private": True,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d dist"
  },
  "dependencies": {
    "framer-motion": "^11.3.30",
    "lucide-react": "^0.460.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.26.2"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "gh-pages": "^6.2.0",
    "postcss": "^8.4.44",
    "tailwindcss": "^3.4.10",
    "vite": "^5.4.3"
  }
}
with open(os.path.join(project_root, "package.json"), "w") as f:
    json.dump(package_json, f, indent=2)

# ---------------------- index.html ----------------------
index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Avichal Baweja • Portfolio</title>
    <meta name="description" content="Portfolio of Avichal Baweja — Data, ML, and Modern Web Projects." />
  </head>
  <body class="bg-slate-950">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""
with open(os.path.join(project_root, "index.html"), "w") as f:
    f.write(index_html)

# ---------------------- tailwind & postcss config ----------------------
tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "Avenir", "Helvetica", "Arial", "sans-serif"],
      },
      colors: {
        glass: "rgba(255,255,255,0.08)"
      },
      boxShadow: {
        glow: "0 0 40px rgba(255,255,255,0.06)"
      }
    },
  },
  plugins: [],
}
"""
with open(os.path.join(project_root, "tailwind.config.js"), "w") as f:
    f.write(tailwind_config)

postcss_config = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""
with open(os.path.join(project_root, "postcss.config.js"), "w") as f:
    f.write(postcss_config)

# ---------------------- vite config ----------------------
vite_config = """import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// If deploying to GitHub Pages at https://<user>.github.io/<repo>/, set base to "/<repo>/"
// Example: base: "/avichal-portfolio/"
export default defineConfig({
  plugins: [react()],
  // base: "/avichal-portfolio/"
});
"""
with open(os.path.join(project_root, "vite.config.js"), "w") as f:
    f.write(vite_config)

# ---------------------- styles ----------------------
index_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --accent: 255, 115, 179; /* pink */
  --accent-2: 56, 189, 248; /* sky */
}

html, body, #root { height: 100%; }

/* Subtle glass card */
.card {
  @apply bg-glass backdrop-blur-xl border border-white/10 rounded-2xl shadow-glow;
}

/* Gradient text helper */
.gradient-text {
  background: linear-gradient(135deg, rgb(var(--accent)), rgb(var(--accent-2)));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
"""
with open(os.path.join(src_dir, "index.css"), "w") as f:
    f.write(index_css)

# ---------------------- main.jsx ----------------------
main_jsx = """import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import App from "./App.jsx";
import Home from "./pages/Home.jsx";
import About from "./pages/About.jsx";
import Experience from "./pages/Experience.jsx";
import Projects from "./pages/Projects.jsx";
import Skills from "./pages/Skills.jsx";
import Contact from "./pages/Contact.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { index: true, element: <Home /> },
      { path: "about", element: <About /> },
      { path: "experience", element: <Experience /> },
      { path: "projects", element: <Projects /> },
      { path: "skills", element: <Skills /> },
      { path: "contact", element: <Contact /> },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
"""
with open(os.path.join(src_dir, "main.jsx"), "w") as f:
    f.write(main_jsx)

# ---------------------- App.jsx + components ----------------------
app_jsx = """import { Outlet, NavLink } from "react-router-dom";
import { motion } from "framer-motion";
import { Github, Linkedin, Mail } from "lucide-react";
import GradientBG from "./components/GradientBG.jsx";

const NavItem = ({ to, label }) => (
  <NavLink
    to={to}
    className={({ isActive }) =>
      `px-3 py-2 rounded-xl transition hover:bg-white/10 ${isActive ? "bg-white/15 text-white" : "text-white/80"}`
    }
  >
    {label}
  </NavLink>
);

export default function App() {
  return (
    <div className="min-h-screen text-white relative overflow-hidden">
      <GradientBG />

      <header className="sticky top-0 z-40 backdrop-blur supports-[backdrop-filter]:bg-slate-900/40">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <NavLink to="/" className="font-bold text-xl gradient-text">Avichal</NavLink>
          <nav className="flex items-center gap-1">
            <NavItem to="/about" label="About" />
            <NavItem to="/experience" label="Experience" />
            <NavItem to="/projects" label="Projects" />
            <NavItem to="/skills" label="Skills" />
            <NavItem to="/contact" label="Contact" />
          </nav>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-10">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className=""
        >
          <Outlet />
        </motion.div>
      </main>

      <footer className="py-8 border-t border-white/10">
        <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-white/60 text-sm">© {new Date().getFullYear()} Avichal Baweja</p>
          <div className="flex gap-3">
            <a className="p-2 rounded-xl hover:bg-white/10" href="https://github.com/Avichal29" target="_blank" rel="noreferrer"><Github size={20} /></a>
            <a className="p-2 rounded-xl hover:bg-white/10" href="https://www.linkedin.com/in/avichalbaweja29" target="_blank" rel="noreferrer"><Linkedin size={20} /></a>
            <a className="p-2 rounded-xl hover:bg-white/10" href="mailto:avichalbaweja@gmail.com"><Mail size={20} /></a>
          </div>
        </div>
      </footer>
    </div>
  );
}
"""
with open(os.path.join(src_dir, "App.jsx"), "w") as f:
    f.write(app_jsx)

gradient_bg = """import { motion } from "framer-motion";

export default function GradientBG() {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 -z-10">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 1.2 }}
        className="absolute -top-40 left-1/2 -translate-x-1/2 w-[1200px] h-[1200px] rounded-full blur-3xl"
        style={{
          background:
            "radial-gradient(800px 800px at 50% 50%, rgba(255, 115, 179, 0.35), transparent 70%), radial-gradient(700px 700px at 70% 30%, rgba(56, 189, 248, 0.25), transparent 60%)",
        }}
      />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(255,255,255,0.06),transparent_60%)]" />
    </div>
  );
}
"""
with open(os.path.join(components_dir, "GradientBG.jsx"), "w") as f:
    f.write(gradient_bg)

# ---------------------- Pages ----------------------
home_jsx = """import { motion } from "framer-motion";
import { NavLink } from "react-router-dom";

export default function Home() {
  return (
    <section className="grid gap-8 md:grid-cols-2 items-center">
      <div className="space-y-6">
        <motion.h1
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-4xl md:text-5xl font-extrabold leading-tight"
        >
          Hi, I'm <span className="gradient-text">Avichal Baweja</span>
        </motion.h1>
        <p className="text-white/80 text-lg">
          Data & ML enthusiast with hands-on experience in predictive modeling, computer vision, and modern web apps.
          I love turning data into actionable insights and building delightful user experiences.
        </p>
        <div className="flex flex-wrap gap-3">
          <NavLink to="/projects" className="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/15">View Projects</NavLink>
          <NavLink to="/contact" className="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/15">Contact Me</NavLink>
        </div>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.1 }}
        className="card p-6"
      >
        <h3 className="text-xl font-semibold mb-3">Quick Info</h3>
        <ul className="grid grid-cols-1 md:grid-cols-2 gap-3 text-white/80">
          <li><span className="text-white/60">Location:</span> India</li>
          <li><span className="text-white/60">Email:</span> avichalbaweja@gmail.com</li>
          <li><span className="text-white/60">LinkedIn:</span> /in/avichalbaweja29</li>
          <li><span className="text-white/60">GitHub:</span> Avichal29</li>
        </ul>
      </motion.div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "Home.jsx"), "w") as f:
    f.write(home_jsx)

about_jsx = """export default function About() {
  return (
    <section className="grid gap-6">
      <div className="card p-6">
        <h2 className="text-2xl font-bold mb-3">About Me</h2>
        <p className="text-white/80">
          Analytical and results-oriented professional with a STEM background and hands-on experience in data analysis,
          predictive modeling, and business operations. Proficient in Python, SQL, and Power BI, with a strong interest
          in data-driven decision-making. Committed to translating complex data into actionable insights that drive
          business performance.
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        <div className="card p-6">
          <h3 className="text-xl font-semibold mb-2">Education</h3>
          <ul className="space-y-3 text-white/80">
            <li>
              <p className="font-medium text-white">Christ University, Bengaluru — B.Tech CSE (Honors in AI & ML)</p>
              <p className="text-white/60">2021 – 2025</p>
            </li>
            <li>
              <p className="font-medium text-white">Delhi Public School, Agra — High School & Senior Secondary</p>
              <p className="text-white/60">2007 – 2021</p>
            </li>
          </ul>
        </div>

        <div className="card p-6">
          <h3 className="text-xl font-semibold mb-2">What I'm Into</h3>
          <p className="text-white/80">
            Machine Learning, Computer Vision, Data Analytics, Full-stack apps with React + FastAPI,
            and building things that help people make better decisions.
          </p>
        </div>
      </div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "About.jsx"), "w") as f:
    f.write(about_jsx)

experience_jsx = """export default function Experience() {
  const roles = [
    {
      title: "Business Analyst",
      company: "Purshotam Profiles Pvt. Ltd.",
      period: "Jan 2025 – Present",
      bullets: [
        "Analyzed and managed sales & marketing processes for Module Mounting Structures.",
        "Prepared data-driven reports, tracked order progress, and evaluated lead performance to improve client satisfaction."
      ]
    },
    {
      title: "Computer Vision Intern",
      company: "TechEagle Innovations Pvt. Ltd.",
      period: "Apr 2024 – May 2024",
      bullets: [
        "Built YOLOv5-powered vision system with real-time feedback control for drone stability, navigation, and obstacle avoidance.",
        "Used Python, OpenCV, PyTorch, and ROS."
      ]
    },
    {
      title: "Junior Software Developer",
      company: "TechEagle Innovations Pvt. Ltd.",
      period: "May 2023 – Jun 2023",
      bullets: [
        "Simulated autonomous drone landing in ROS & Gazebo using Python-based control logic.",
        "Implemented ArUco marker detection with OpenCV for precise coordinate-based landings."
      ]
    },
    {
      title: "IT Intern",
      company: "Sankalptaru Foundation",
      period: "Jan 2023 – Mar 2023",
      bullets: [
        "Developed predictive model to forecast farm conditions using Python, Pandas, scikit-learn, and NumPy.",
        "Performed market analysis with Matplotlib and statistical techniques."
      ]
    },
  ];

  return (
    <section className="grid gap-6">
      <h2 className="text-2xl font-bold">Experience</h2>
      <div className="grid gap-4">
        {roles.map((r, i) => (
          <div key={i} className="card p-6">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-2">
              <div>
                <h3 className="text-xl font-semibold">{r.title} — <span className="text-white/80">{r.company}</span></h3>
              </div>
              <p className="text-white/60">{r.period}</p>
            </div>
            <ul className="list-disc pl-6 mt-3 text-white/80 space-y-2">
              {r.bullets.map((b, j) => <li key={j}>{b}</li>)}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "Experience.jsx"), "w") as f:
    f.write(experience_jsx)

projects_jsx = """export default function Projects() {
  const projects = [
    {
      name: "Forest Management System",
      stack: "Arduino, IR & Temp Sensors, Wi-Fi, Embedded C",
      desc: "Real-time forest monitoring to detect fire, water levels, and temperature; showcased at Microsoft on Arduino Day.",
      link: null
    },
    {
      name: "Event Planner",
      stack: "React, FastAPI, REST",
      desc: "Full-stack app to create, view, and RSVP to events with real-time updates and in-memory data.",
      link: null
    },
    {
      name: "Handwritten to LaTeX",
      stack: "Python, OCR, Image Processing, ML",
      desc: "Mapped handwritten characters to LaTeX commands using OCR and ML techniques.",
      link: null
    },
    {
      name: "Trackpad Control using Hand Gestures",
      stack: "Python, OpenCV, MediaPipe, PyAutoGUI, NumPy",
      desc: "Real-time hand gesture trackpad control with optimized pipeline for responsive interaction.",
      link: null
    },
    {
      name: "Student Academic Performance: Impact on Self Esteem",
      stack: "IBM SPSS",
      desc: "Surveyed students across universities; analyzed correlation between academic scores and self esteem.",
      link: null
    },
  ];

  return (
    <section className="grid gap-6">
      <h2 className="text-2xl font-bold">Projects</h2>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((p, i) => (
          <div key={i} className="card p-6 hover:translate-y-[-2px] transition">
            <h3 className="text-lg font-semibold">{p.name}</h3>
            <p className="text-white/60 text-sm mt-1">{p.stack}</p>
            <p className="text-white/80 mt-3">{p.desc}</p>
            {p.link && <a className="mt-4 inline-block px-3 py-2 rounded-lg bg-white/10 hover:bg-white/15" href={p.link} target="_blank" rel="noreferrer">View</a>}
          </div>
        ))}
      </div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "Projects.jsx"), "w") as f:
    f.write(projects_jsx)

skills_jsx = """export default function Skills() {
  const skills = [
    "Python", "MySQL", "MongoDB", "Power BI", "C", "Java (basics)",
    "UI Path", "Machine Learning", "Data Analysis", "Tableau",
    "React", "FastAPI", "HTML", "CSS"
  ];

  return (
    <section className="grid gap-6">
      <h2 className="text-2xl font-bold">Skills</h2>
      <div className="card p-6">
        <div className="flex flex-wrap gap-3">
          {skills.map((s, i) => (
            <span key={i} className="px-3 py-2 rounded-xl bg-white/10 text-white/90 text-sm">{s}</span>
          ))}
        </div>
      </div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "Skills.jsx"), "w") as f:
    f.write(skills_jsx)

contact_jsx = """export default function Contact() {
  return (
    <section className="grid gap-6">
      <h2 className="text-2xl font-bold">Contact</h2>
      <div className="card p-6">
        <div className="grid sm:grid-cols-2 gap-4 text-white/80">
          <p><span className="text-white/60">Email:</span> <a className="underline decoration-white/30 hover:decoration-white" href="mailto:avichalbaweja@gmail.com">avichalbaweja@gmail.com</a></p>
          <p><span className="text-white/60">LinkedIn:</span> <a className="underline decoration-white/30 hover:decoration-white" href="https://www.linkedin.com/in/avichalbaweja29" target="_blank" rel="noreferrer">/in/avichalbaweja29</a></p>
          <p><span className="text-white/60">GitHub:</span> <a className="underline decoration-white/30 hover:decoration-white" href="https://github.com/Avichal29" target="_blank" rel="noreferrer">@Avichal29</a></p>
          <p><span className="text-white/60">Phone:</span> +91 9837452284</p>
        </div>
      </div>
    </section>
  );
}
"""
with open(os.path.join(pages_dir, "Contact.jsx"), "w") as f:
    f.write(contact_jsx)

# ---------------------- README ----------------------
readme_md = """# Avichal Baweja — Portfolio (React + Vite + Tailwind + Framer Motion)

Modern multi-page portfolio with animated gradients, glass cards, and responsive design.

## 🛠️ Tech
- React 18 + Vite
- Tailwind CSS
- Framer Motion (animations)
- React Router (multi-page)
- Lucide icons

## ▶️ Run locally
```bash
npm install
npm run dev
