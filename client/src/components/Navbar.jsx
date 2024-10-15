import React from "react";
import { Link } from "react-router-dom";
import DarkModeToggle from "./DarkModeToggle";
import { FiLogOut  } from "react-icons/fi"; 

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between p-4 px-32 bg-white dark:bg-slate-900 shadow-md">
      <div className="flex items-center">
        <div className="text-xl font-bold text-gray-800 dark:text-white">
          <Link to="/"> Behavior Analysis</Link>
        </div>
      </div>
      <div className="space-x-4 text-xl">
        <Link
          to="/activity"
          className="text-gray-800 dark:text-gray-200 hover:text-blue-500"
        >
          Activity
        </Link>
        <Link
          to="/search"
          className="text-gray-800 dark:text-gray-200 hover:text-blue-500"
        >
          Search
        </Link>
      </div>
      <div className="flex items-center space-x-2">
      <DarkModeToggle />
        <Link
          to="/logout"
          className="text-gray-800 dark:text-gray-200 hover:text-blue-500 flex items-center"
        >
          <FiLogOut  className="ml-10 text-3xl" /> 
        </Link>

      </div>
    </nav>
  );
}
