import { Product } from './types';

export const PRODUCTS: Product[] = [
  // HEAT PUMPS - x-change dynamic eco (Page 11)
  {
    id: 'eco-s',
    articleNumber: 'W20528',
    name: 'x-change dynamic eco S',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 6990.00,
    description: 'Modulierende Luft/Wasser-Wärmepumpe, R290 Propan.',
    efficiency: 'A+++ / A+++',
    power: '3,0 - 8,0 kW',
    cop: '4,48',
    compatibleWith: ['W40853'] // Hydrobox eco
  },
  {
    id: 'eco-m',
    articleNumber: 'W20529',
    name: 'x-change dynamic eco M',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 7490.00,
    description: 'Modulierende Luft/Wasser-Wärmepumpe, R290 Propan.',
    efficiency: 'A+++ / A+++',
    power: '3,0 - 10,3 kW',
    cop: '4,44',
    compatibleWith: ['W40853']
  },
  {
    id: 'eco-l',
    articleNumber: 'W20530',
    name: 'x-change dynamic eco L',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 7990.00,
    description: 'Modulierende Luft/Wasser-Wärmepumpe, R290 Propan.',
    efficiency: 'A+++ / A+++',
    power: '5,0 - 14,0 kW',
    cop: '4,29',
    compatibleWith: ['W40853']
  },

  // HEAT PUMPS - x-change dynamic pro (Page 15)
  {
    id: 'pro-s',
    articleNumber: 'W20501',
    name: 'x-change dynamic pro S',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 11990.00,
    description: 'Höchste Effizienz, geringste Schallemissionen, R290.',
    efficiency: 'A+++ / A+++',
    power: '2,9 - 8,0 kW',
    cop: '4,96',
    compatibleWith: ['W40716', 'W30295'] // Hydrobox pro, x-buffer combi pro
  },
  {
    id: 'pro-m',
    articleNumber: 'W20502',
    name: 'x-change dynamic pro M',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 13500.00,
    description: 'Höchste Effizienz, geringste Schallemissionen, R290.',
    efficiency: 'A+++ / A+++',
    power: '4,9 - 13,2 kW',
    cop: '4,95',
    compatibleWith: ['W40716', 'W30295']
  },
  {
    id: 'pro-l',
    articleNumber: 'W20503',
    name: 'x-change dynamic pro L',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen',
    price: 18700.00,
    description: 'Höchste Effizienz, geringste Schallemissionen, R290.',
    efficiency: 'A+++ / A+++',
    power: '8,0 - 21,3 kW',
    cop: '4,80',
    compatibleWith: ['W40716']
  },

  // HEAT PUMPS - x-change dynamic pro ac AW E (Page 19)
  {
    id: 'pro-ac-6',
    articleNumber: 'W20447',
    name: 'x-change dynamic pro ac 6 AW E',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen (Kühlen)',
    price: 12023.00,
    description: 'Heizen und Kühlen, modulierend.',
    efficiency: 'A+++ / A+++',
    power: '3,5 - 7,5 kW',
    cop: '4,66',
    compatibleWith: ['W30295']
  },
  {
    id: 'pro-ac-10',
    articleNumber: 'W20448',
    name: 'x-change dynamic pro ac 10 AW E',
    category: 'heatpump',
    subCategory: 'Luft/Wasser Außen (Kühlen)',
    price: 13472.00,
    description: 'Heizen und Kühlen, modulierend.',
    efficiency: 'A+++ / A+++',
    power: '4,9 - 15,0 kW',
    cop: '4,80',
    compatibleWith: ['W30295']
  },

  // STORAGE - x-buffer combi (Page 53)
  {
    id: 'buffer-combi',
    articleNumber: 'W30265',
    name: 'x-buffer combi',
    category: 'storage',
    subCategory: 'Puffer- & Warmwasser',
    price: 6136.00,
    description: 'Pufferspeicher 127L, Warmwasserspeicher 231L.',
    efficiency: 'B'
  },
  {
    id: 'buffer-combi-pro',
    articleNumber: 'W30295',
    name: 'x-buffer combi pro',
    category: 'storage',
    subCategory: 'Puffer- & Warmwasser',
    price: 9038.00,
    description: 'Inkl. Regelung für x-change dynamic pro.',
    efficiency: 'B'
  },
  {
    id: 'buffer-fresh-200',
    articleNumber: 'W30201',
    name: 'x-buffer fresh 200',
    category: 'storage',
    subCategory: 'Warmwasser',
    price: 1980.00,
    description: 'Hochleistungsspeicher für Trinkwassererwärmung.',
    efficiency: 'B'
  },

  // HYDRAULICS (Page 85, 87)
  {
    id: 'hydrobox-eco',
    articleNumber: 'W40853',
    name: 'Hydrobox eco',
    category: 'hydraulics',
    price: 3490.00,
    description: 'Zentrale Regel- und Steuereinheit für dynamic eco.',
    compatibleWith: ['W20528', 'W20529', 'W20530'] // eco S, M, L
  },
  {
    id: 'hydrobox-pro',
    articleNumber: 'W40716',
    name: 'Hydrobox pro',
    category: 'hydraulics',
    price: 4990.00,
    description: 'Zentrale Regel- und Steuereinheit für dynamic pro.',
    compatibleWith: ['W20501', 'W20502', 'W20503', 'W20447', 'W20448', 'W20449'] // pro S, M, L, ac 6, 10, 16
  },
  {
    id: 'x-center-pro',
    articleNumber: 'W40675',
    name: 'x-center pro Wandregler',
    category: 'hydraulics',
    price: 2914.00,
    description: 'Wärmepumpen-Wandregler mit 7" Touch-Display.',
    compatibleWith: ['W20501', 'W20502', 'W20503'] // pro series
  },

  // ACCESSORIES (Page 12, 16, 20)
  {
    id: 'acc-cover-eco',
    articleNumber: 'W40731',
    name: 'Anschlussabdeckung eco S/M/L',
    category: 'accessory',
    price: 195.00,
    description: 'Schutz der Anschlussleitungen vor Witterung.'
  },
  {
    id: 'acc-magnetit',
    articleNumber: 'W40451',
    name: 'Magnetitschlammabscheider DN 32',
    category: 'accessory',
    price: 307.00,
    description: 'Entfernt Schmutzpartikel bis 4μm.'
  },
  {
    id: 'acc-frost',
    articleNumber: 'W40732',
    name: 'Frostschutzventilset 1 1/4"',
    category: 'accessory',
    price: 295.00,
    description: 'Thermostatische Sicherheitsventile.'
  },

  // SERVICES (Page 98)
  {
    id: 'srv-commissioning',
    articleNumber: '9985238',
    name: 'Inbetriebnahme Wärmepumpe',
    category: 'service',
    price: 335.00,
    description: 'Überprüfung und Konfiguration durch Werkskundendienst.'
  },
  {
    id: 'srv-travel',
    articleNumber: '9980509',
    name: 'Servicepauschale Vor-Ort-Einsatz',
    category: 'service',
    price: 125.00,
    description: 'Anfahrtspauschale für Serviceeinsätze.'
  }
];
