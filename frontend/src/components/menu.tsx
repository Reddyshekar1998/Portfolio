import React, { useState } from 'react';

// Define types
type About = {
  name: string;
  title: string;
  description: string;
  email: string;
  location: string;
};

type Project = {
  title: string;
  description: string;
  link: string;
};

// AboutCard component (as provided, unchanged)
type AboutProps = {
  about: About;
};

export const AboutCard: React.FC<AboutProps> = ({ about }) => (
  <div className="bg-white rounded-2xl shadow p-6 text-center">
    <h2 className="text-2xl font-bold mb-2">{about.name}</h2>
    <p className="text-primary font-semibold">{about.title}</p>
    <p className="mt-2 text-gray-600">{about.description}</p>
    <p className="mt-2 text-gray-500">📧 {about.email}</p>
    <p className="text-gray-500">📍 {about.location}</p>
  </div>
);

// Main Portfolio Component
const Portfolio: React.FC = () => {
  // Sample data (replace with your own)
  const aboutData: About = {
    name: 'Your Name',
    title: 'Web Developer',
    description: 'Passionate about creating user-friendly web applications. Skilled in React, TypeScript, and modern web technologies.',
    email: 'your.email@example.com',
    location: 'Your City, Country',
  };

  const [projects] = useState<Project[]>([
    { title: 'Project 1', description: 'Description of project 1.', link: '#' },
    { title: 'Project 2', description: 'Description of project 2.', link: '#' },
    { title: 'Project 3', description: 'Description of project 3.', link: '#' },
  ]);

  const scrollToSection = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="font-sans text-gray-800">
      {/* Header */}
      <header className="bg-gray-800 text-white p-4 text-center">
        <h1 className="text-3xl font-bold">{aboutData.name}</h1>
        <nav className="mt-4">
          <button onClick={() => scrollToSection('hero')} className="text-white mx-4 hover:underline">Home</button>
          <button onClick={() => scrollToSection('about')} className="text-white mx-4 hover:underline">About</button>
          <button onClick={() => scrollToSection('projects')} className="text-white mx-4 hover:underline">Projects</button>
          <button onClick={() => scrollToSection('contact')} className="text-white mx-4 hover:underline">Contact</button>
        </nav>
      </header>

      {/* Hero Section */}
      <section id="hero" className="bg-gray-100 text-center py-16 px-8">
        <h2 className="text-4xl font-bold mb-4">Welcome to My Portfolio</h2>
        <p className="text-lg">I'm a {aboutData.title} passionate about building amazing web experiences. Check out my work below.</p>
      </section>

      {/* About Section */}
      <section id="about" className="py-16 px-8 max-w-4xl mx-auto">
        <AboutCard about={aboutData} />
      </section>

      {/* Projects Section */}
      <section id="projects" className="py-16 px-8 max-w-6xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-8">My Projects</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {projects.map((project, index) => (
            <div key={index} className="border border-gray-300 p-4 rounded-lg">
              <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
              <p className="text-gray-600 mb-4">{project.description}</p>
              <a href={project.link} className="text-blue-500 hover:underline">View Demo</a>
            </div>
          ))}
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-16 px-8 max-w-4xl mx-auto text-center">
        <h2 className="text-3xl font-bold mb-4">Contact Me</h2>
        <p className="mb-2">Email: {aboutData.email}</p>
        <p className="mb-2">LinkedIn: <a href="#" className="text-blue-500 hover:underline">Your LinkedIn</a></p>
        <p>GitHub: <a href="#" className="text-blue-500 hover:underline">Your GitHub</a></p>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white text-center py-4">
        <p>&copy; 2024 {aboutData.name}. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Portfolio;