'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAppSelector, useAppDispatch } from '@/store/hooks';
import { logout } from '@/store/slices/authSlice';

export function Header() {
  const router = useRouter();
  const dispatch = useAppDispatch();
  const { user, token } = useAppSelector(state => state.auth);
  const { items } = useAppSelector(state => state.cart);

  const handleLogout = () => {
    dispatch(logout());
    router.push('/');
  };

  return (
    <header className="bg-primary text-white shadow-lg">
      <nav className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <Link href="/" className="text-2xl font-bold">
          PassMark
        </Link>
        
        <div className="flex items-center gap-6">
          <Link href="/products" className="hover:text-gray-200">
            Products
          </Link>
          
          <Link href="/cart" className="hover:text-gray-200">
            Cart ({items.length})
          </Link>
          
          {token && user ? (
            <div className="flex items-center gap-4">
              <span>{user.firstName}</span>
              <Link href="/profile" className="hover:text-gray-200">
                Profile
              </Link>
              <button
                onClick={handleLogout}
                className="bg-red-500 px-4 py-2 rounded hover:bg-red-600"
              >
                Logout
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-4">
              <Link href="/login" className="hover:text-gray-200">
                Login
              </Link>
              <Link
                href="/register"
                className="bg-secondary px-4 py-2 rounded hover:bg-opacity-80"
              >
                Register
              </Link>
            </div>
          )}
        </div>
      </nav>
    </header>
  );
}
