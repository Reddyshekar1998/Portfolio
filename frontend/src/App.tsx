// src/App.tsx

import { useEffect, useState } from "react";
import { Routes, Route, Link } from "react-router-dom";
import { AboutCard } from "./components/AboutCard";
import { SkillsList } from "./components/SkillsList";
import { ProjectList } from "./components/ProjectList";
import { AddProjectForm } from "./components/AddProjectForm";

// Type Definitions
type About = {
  name: string;
  title: string;
  description: string;
  email: string;
  location: string;
};

type Skill = {
  id: number;
  name: string;
};

type Project = {
  id: number;
  name: string;
  description: string;
  tech_stack: string[];
};

function App() {
  const [about, setAbout] = useState<About | null>(null);
  const [skills, setSkills] = useState<Skill[]>([]);
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/about")
      .then((res) => res.json())
      .then((data: About) => setAbout(data));

    fetch("http://localhost:8000/skills")
      .then((res) => res.json())
      .then((data: Skill[]) => setSkills(data));

    fetch("http://localhost:8000/projects")
      .then((res) => res.json())
      .then((data: Project[]) => setProjects(data));
  }, []);

  const addProject = (project: Project) => {
    fetch("http://localhost:8000/projects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(project),
    })
      .then((res) => res.json())
      .then((newProject: Project) => setProjects([...projects, newProject]));
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <header className="bg-white shadow">
        <div className="max-w-3xl mx-auto p-4 flex justify-between items-center">
          <h1 className="text-xl font-bold text-gray-800">
            Kilari Reddy Sekhar Portfolio
          </h1>
          <nav className="space-x-4">
            <Link to="/" className="text-blue-600 hover:underline">
              About
            </Link>
            <Link to="/skills" className="text-blue-600 hover:underline">
              Skills
            </Link>
            <Link to="/projects" className="text-blue-600 hover:underline">
              Projects
            </Link>
          </nav>
        </div>
      </header>

      <main className="flex-grow max-w-3xl mx-auto p-4 space-y-6">
        <Routes>
          <Route
            path="/"
            element={about ? <AboutCard about={about} /> : <div>Loading...</div>}
          />
          <Route path="/skills" element={<SkillsList skills={skills} />} />
          <Route
            path="/projects"
            element={
              <div className="space-y-6">
                <ProjectList projects={projects} />
                <AddProjectForm onAdd={addProject} />
              </div>
            }
          />
        </Routes>
      </main>

      <footer className="text-center text-gray-500 text-sm py-4">
        © {new Date().getFullYear()} Kilari Reddy Sekhar. All rights reserved.
      </footer>
    </div>
  );
}

export default App;
