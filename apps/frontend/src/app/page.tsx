'use client';

export default function HomePage() {
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary to-secondary text-white py-20">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <h1 className="text-5xl font-bold mb-4">Welcome to PassMark</h1>
          <p className="text-xl mb-8">Discover amazing products at unbeatable prices</p>
          <a
            href="/products"
            className="bg-white text-primary px-8 py-3 rounded-lg font-bold hover:bg-gray-100 inline-block"
          >
            Shop Now
          </a>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4">
          <h2 className="text-4xl font-bold text-center mb-12">Why Choose PassMark?</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow text-center">
              <div className="text-4xl mb-4">🚚</div>
              <h3 className="text-2xl font-bold mb-2">Fast Shipping</h3>
              <p className="text-gray-600">Get your orders delivered quickly and securely</p>
            </div>
            
            <div className="bg-white p-8 rounded-lg shadow text-center">
              <div className="text-4xl mb-4">💰</div>
              <h3 className="text-2xl font-bold mb-2">Best Prices</h3>
              <p className="text-gray-600">Competitive pricing on all our products</p>
            </div>
            
            <div className="bg-white p-8 rounded-lg shadow text-center">
              <div className="text-4xl mb-4">🛡️</div>
              <h3 className="text-2xl font-bold mb-2">Secure Payment</h3>
              <p className="text-gray-600">Your transactions are safe and protected</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-primary text-white py-16">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to start shopping?</h2>
          <a
            href="/products"
            className="bg-white text-primary px-8 py-3 rounded-lg font-bold hover:bg-gray-100 inline-block"
          >
            Browse Products
          </a>
        </div>
      </section>
    </div>
  );
}
