import React from "react";

type SkillsProps = {
  skills: string[];
};

export const SkillsList: React.FC<SkillsProps> = ({ skills }) => (
  <div className="bg-white rounded-2xl shadow p-6">
    <h3 className="text-xl font-semibold mb-4">Skills</h3>
    <div className="flex flex-wrap gap-2">
      {skills.map((skill, idx) => (
        <span
          key={idx}
          className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm"
        >
          {skill}
        </span>
      ))}
    </div>
  </div>
);