import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate(); 

    const handleSubmit = (e) => {
        e.preventDefault();
        setError('');

        if (password === 'Admin@123') {
            localStorage.setItem('userId', username);
            navigate('/activity'); 
        } else {
            setError('Invalid password!');
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-800">
            <div className="bg-gray-900 rounded-lg p-8 shadow-md w-96">
                <h2 className="text-2xl text-white mb-6 text-center">Login</h2>
                <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                    <input
                        type="email"
                        placeholder="Email"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="p-2 bg-gray-700 text-white rounded"
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="p-2 bg-gray-700 text-white rounded"
                        required
                    />
                    <button
                        type="submit"
                        className="bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition"
                    >
                        Submit
                    </button>
                </form>
                {error && <p className="text-red-500 mt-4 text-center">{error}</p>}
            </div>
        </div>
    );
};

export default Login;
