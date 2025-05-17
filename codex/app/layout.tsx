import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Kushal Banda | Portfolio",
  description: "Personal portfolio of Kushal Banda, AI Engineer & Cloud Architect",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased scroll-smooth`}>
        <header className="w-full bg-gradient-to-r from-purple-700 to-black py-4">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <h1 className="text-2xl font-bold text-white">Kushal Banda</h1>
            <nav className="space-x-6">
              <a href="#home" className="text-white hover:text-gray-200">Home</a>
              <a href="#about" className="text-white hover:text-gray-200">About</a>
              <a href="#skills" className="text-white hover:text-gray-200">Skills</a>
              <a href="#projects" className="text-white hover:text-gray-200">Projects</a>
              <a href="#contact" className="text-white hover:text-gray-200">Contact</a>
            </nav>
          </div>
        </header>
        {children}
      </body>
    </html>
  );
}
