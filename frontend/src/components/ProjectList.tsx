import React from "react";

type Project = {
  name: string;
  description: string;
  tech_stack: string[];
};

type ProjectListProps = {
  projects: Project[];
};

export const ProjectList: React.FC<ProjectListProps> = ({ projects }) => (
  <div className="bg-white rounded-2xl shadow p-6">
    <h3 className="text-xl font-semibold mb-4">Projects</h3>
    <div className="grid md:grid-cols-2 gap-4">
      {projects.map((project, idx) => (
        <div key={idx} className="border rounded-xl p-4 hover:shadow-lg transition">
          <h4 className="font-semibold text-lg mb-1">{project.name}</h4>
          <p className="text-gray-600 mb-2">{project.description}</p>
          <div className="flex flex-wrap gap-1">
            {project.tech_stack.map((tech, i) => (
              <span
                key={i}
                className="bg-green-100 text-green-800 px-2 py-0.5 rounded-full text-xs"
              >
                {tech}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  </div>
);