export default function Home() {
  return (
    <main className="flex flex-col">
      {/* Home / Hero */}
      <section id="home" className="bg-gradient-to-r from-purple-700 to-black text-white py-20">
        <div className="container mx-auto px-6 text-center">
          <h1 className="text-6xl font-bold mb-4">Kushal Banda</h1>
          <p className="text-2xl mb-6">AI Engineer & Cloud Architect</p>
          <p className="max-w-2xl mx-auto mb-8 text-gray-200">
            Building cutting-edge AI solutions and scalable cloud infrastructure.
          </p>
          <div className="flex justify-center space-x-4 mb-8">
            <a
              href="/resume.pdf"
              className="bg-white text-purple-700 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
            >
              Download Resume
            </a>
            <a
              href="#contact"
              className="bg-purple-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-purple-700 transition"
            >
              Contact Me
            </a>
          </div>
          <div className="flex justify-center space-x-6 mb-8">
            <a href="https://github.com/kushalbanda" className="text-white hover:text-gray-300">GitHub</a>
            <a href="https://linkedin.com/in/kushalbanda" className="text-white hover:text-gray-300">LinkedIn</a>
            <a href="https://twitter.com/kushalbanda" className="text-white hover:text-gray-300">Twitter</a>
          </div>
        </div>
      </section>

      {/* About */}
      <section id="about" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-6">About Me</h2>
          <p className="max-w-3xl mx-auto text-center text-gray-700">
            I'm Kushal Banda, an AI Engineer and Cloud Architect specializing in Generative AI, AWS, and DevOps.
            I design and build scalable solutions that leverage machine learning and cloud infrastructure to
            drive innovation and solve real-world challenges.
          </p>
        </div>
      </section>

      {/* Skills */}
      <section id="skills" className="bg-gray-50 py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-10">Skills</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
            {['AI', 'Generative AI', 'Machine Learning', 'AWS', 'DevOps', 'Docker', 'Kubernetes', 'Python', 'TypeScript', 'Terraform', 'CI/CD'].map((skill) => (
              <span key={skill} className="block text-center bg-purple-600 text-white py-2 rounded-full">
                {skill}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Projects */}
      <section id="projects" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-10">Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="border rounded-lg p-6 hover:shadow-lg transition">
              <h3 className="text-2xl font-semibold mb-2">Project One</h3>
              <p className="text-gray-600">A brief description of the project that highlights AI and AWS integration.</p>
              <a href="#" className="text-purple-600 hover:underline mt-2 inline-block">View Details</a>
            </div>
            <div className="border rounded-lg p-6 hover:shadow-lg transition">
              <h3 className="text-2xl font-semibold mb-2">Project Two</h3>
              <p className="text-gray-600">A brief description of another project showcasing DevOps automation.</p>
              <a href="#" className="text-purple-600 hover:underline mt-2 inline-block">View Details</a>
            </div>
            <div className="border rounded-lg p-6 hover:shadow-lg transition">
              <h3 className="text-2xl font-semibold mb-2">Cloud Monitoring Dashboard</h3>
              <p className="text-gray-600">A real-time dashboard for monitoring AWS services and resource utilization.</p>
              <a href="#" className="text-purple-600 hover:underline mt-2 inline-block">View Details</a>
            </div>
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="bg-gray-50 py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-6">Contact</h2>
          <p className="text-center text-gray-700 mb-4">Feel free to reach out for collaborations or just a friendly chat.</p>
          <div className="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-4">
            <a
              href="mailto:kushal@example.com"
              className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 transition"
            >
              Email Me
            </a>
            <a
              href="tel:+1234567890"
              className="bg-white text-purple-600 px-6 py-3 rounded-lg border border-purple-600 hover:bg-purple-50 transition"
            >
              Call Me
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-purple-700 to-black text-white py-6">
        <div className="container mx-auto px-6 text-center">
          &copy; {new Date().getFullYear()} Kushal Banda. All rights reserved.
        </div>
      </footer>
    </main>
  );
}
