'use client';

import { useEffect } from 'react';
import { useAppDispatch, useAppSelector } from '@/store/hooks';
import { setProducts, setLoading } from '@/store/slices/productsSlice';
import { productsAPI } from '@/lib/api';
import { ProductCard } from '@/components/ProductCard';

export default function ProductsPage() {
  const dispatch = useAppDispatch();
  const { items, isLoading } = useAppSelector(state => state.products);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        dispatch(setLoading(true));
        const response = await productsAPI.getAll();
        dispatch(setProducts(response.data));
      } catch (error) {
        console.error('Failed to fetch products:', error);
      } finally {
        dispatch(setLoading(false));
      }
    };

    fetchProducts();
  }, [dispatch]);

  if (isLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="text-center">Loading products...</div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">Our Products</h1>
      
      {items.length === 0 ? (
        <div className="text-center text-gray-500 py-12">
          No products available
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {items.map(product => (
            <ProductCard key={product._id} {...product} />
          ))}
        </div>
      )}
    </div>
  );
}
