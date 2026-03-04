export interface Product {
  id: string;
  articleNumber: string;
  name: string;
  category: 'heatpump' | 'storage' | 'hydraulics' | 'accessory' | 'service';
  subCategory?: string;
  price: number;
  description: string;
  efficiency?: string; // e.g. A+++
  power?: string; // e.g. 3,0 - 8,0 kW
  cop?: string; // e.g. 4,48
  compatibleWith?: string[]; // article numbers or categories
}

export interface Configuration {
  heatPump?: Product;
  storage?: Product;
  hydraulics?: Product;
  accessories: Product[];
  services: Product[];
}
