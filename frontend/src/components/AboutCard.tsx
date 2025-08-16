import React from "react";

type AboutProps = {
  about: {
    name: string;
    title: string;
    description: string;
    email: string;
    location: string;
  };
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