import React, { useState } from "react";

type Project = {
  name: string;
  description: string;
  tech_stack: string[];
};

type AddProjectFormProps = {
  onAdd: (project: Project) => void;
};

export const AddProjectForm: React.FC<AddProjectFormProps> = ({ onAdd }) => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [techStack, setTechStack] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !description || !techStack) {
      alert("Please fill in all fields.");
      return;
    }
    onAdd({ name, description, tech_stack: techStack.split(",").map(t => t.trim()) });
    setName("");
    setDescription("");
    setTechStack("");
  };

  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h3 className="text-xl font-semibold mb-4">Add New Project</h3>
      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          type="text"
          placeholder="Project Name"
          value={name}
          onChange={e => setName(e.target.value)}
          className="w-full border rounded px-3 py-2"
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={e => setDescription(e.target.value)}
          className="w-full border rounded px-3 py-2"
        />
        <input
          type="text"
          placeholder="Tech stack (comma separated)"
          value={techStack}
          onChange={e => setTechStack(e.target.value)}
          className="w-full border rounded px-3 py-2"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Add Project
        </button>
      </form>
    </div>
  );
};