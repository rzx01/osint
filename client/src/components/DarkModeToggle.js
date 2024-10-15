
import React, { useEffect } from 'react';
import { useRecoilState } from 'recoil';
import { darkModeAtom } from '../atoms/darkModeAtom';
import { FaSun, FaMoon } from 'react-icons/fa';

export default function DarkModeToggle() {
  const [darkMode, setDarkMode] = useRecoilState(darkModeAtom);

  useEffect(() => {
    const savedMode = localStorage.getItem('darkMode') === 'true';
    setDarkMode(savedMode);
    document.documentElement.classList.toggle('dark', savedMode);
  }, [setDarkMode]);

  const toggleDarkMode = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);
    localStorage.setItem('darkMode', newMode);
    document.documentElement.classList.toggle('dark', newMode);
  };

  return (
    <button
      onClick={toggleDarkMode}
      className="p-2 rounded bg-gray-200 dark:bg-gray-800 text-gray-800 dark:text-gray-200"
    >
      {darkMode ? <FaSun size={24} /> : <FaMoon size={24} />}
    </button>
  );
}
