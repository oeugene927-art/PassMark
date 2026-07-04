import type { Metadata } from 'next';
import { Header } from '@/components/Header';
import { Footer } from '@/components/Footer';
import { ReduxProvider } from '@/providers/ReduxProvider';
import '@/styles/globals.css';

export const metadata: Metadata = {
  title: 'PassMark - E-Commerce Platform',
  description: 'Shop the best products at PassMark',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ReduxProvider>
          <Header />
          <main className="min-h-screen">{children}</main>
          <Footer />
        </ReduxProvider>
      </body>
    </html>
  );
}
