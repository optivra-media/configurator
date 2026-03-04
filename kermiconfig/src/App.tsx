/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useMemo, useRef } from 'react';
import { 
  ChevronRight, 
  ChevronLeft, 
  CheckCircle2, 
  AlertCircle, 
  ShoppingCart, 
  Printer, 
  Download, 
  Info,
  Thermometer,
  Zap,
  ShieldCheck,
  Wrench,
  X,
  Plus,
  Minus
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { PRODUCTS } from './data';
import { Product, Configuration } from './types';

const STEPS = [
  { id: 'heatpump', label: 'Wärmepumpe', icon: Thermometer },
  { id: 'storage', label: 'Speicher', icon: ShieldCheck },
  { id: 'hydraulics', label: 'Hydraulik & Regelung', icon: Zap },
  { id: 'accessories', label: 'Zubehör', icon: Plus },
  { id: 'services', label: 'Service', icon: Wrench },
  { id: 'summary', label: 'Zusammenfassung', icon: ShoppingCart },
];

interface ProductCardProps {
  product: Product;
  isSelected: boolean;
  onSelect: () => void;
  isDisabled?: boolean;
  isMulti?: boolean;
  key?: React.Key;
}

const ProductCard: React.FC<ProductCardProps> = ({ 
  product, 
  isSelected, 
  onSelect, 
  isDisabled, 
  isMulti 
}) => {
  return (
    <div 
      onClick={() => !isDisabled && onSelect()}
      className={`relative p-4 md:p-6 rounded-xl md:rounded-2xl border-2 transition-all cursor-pointer flex flex-col gap-3 md:gap-4 ${
        isDisabled 
          ? 'opacity-40 grayscale cursor-not-allowed border-slate-100 bg-slate-50' 
          : isSelected 
            ? 'border-[#A5CF4C] bg-[#A5CF4C]/5 shadow-md' 
            : 'border-slate-100 hover:border-slate-200 hover:shadow-sm'
      }`}
    >
      <div className="flex justify-between items-start">
        <div className="min-w-0">
          <p className="text-[9px] md:text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-0.5 md:mb-1">{product.subCategory || product.category}</p>
          <h4 className="font-bold text-slate-900 leading-tight text-sm md:text-base truncate md:whitespace-normal">{product.name}</h4>
          <p className="text-[10px] md:text-xs text-slate-500 mt-0.5 md:mt-1">Art.-Nr: {product.articleNumber}</p>
        </div>
        <div className={`p-1 rounded-full shrink-0 ${isSelected ? 'bg-[#A5CF4C] text-white' : 'bg-slate-100 text-slate-300'}`}>
          {isMulti ? (isSelected ? <X size={14} md:size={16} /> : <Plus size={14} md:size={16} />) : <CheckCircle2 size={16} md:size={20} />}
        </div>
      </div>

      <p className="text-xs md:text-sm text-slate-600 line-clamp-2">{product.description}</p>

      {product.efficiency && (
        <div className="flex gap-3 md:gap-4">
          <div className="flex items-center gap-1 md:gap-1.5">
            <div className="bg-emerald-500 text-white text-[8px] md:text-[10px] font-bold px-1 md:px-1.5 py-0.5 rounded">
              {product.efficiency}
            </div>
            <span className="text-[8px] md:text-[10px] text-slate-400 font-bold uppercase">Effizienz</span>
          </div>
          {product.cop && (
            <div className="flex items-center gap-1 md:gap-1.5">
              <span className="text-[10px] md:text-xs font-bold text-slate-700">{product.cop}</span>
              <span className="text-[8px] md:text-[10px] text-slate-400 font-bold uppercase">COP</span>
            </div>
          )}
        </div>
      )}

      <div className="mt-auto pt-3 md:pt-4 flex items-center justify-between border-t border-slate-100/50">
        <span className="text-base md:text-lg font-mono font-bold text-slate-900">
          {product.price.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
        </span>
        {isDisabled && (
          <div className="flex items-center gap-1 text-amber-600">
            <AlertCircle size={12} md:size={14} />
            <span className="text-[8px] md:text-[10px] font-bold uppercase">Inkompatibel</span>
          </div>
        )}
      </div>
    </div>
  );
};

const SummaryView: React.FC<{ config: Configuration, total: number, onPrint: () => void }> = ({ config, total, onPrint }) => {
  const items = [
    config.heatPump,
    config.storage,
    config.hydraulics,
    ...config.accessories,
    ...config.services
  ].filter(Boolean) as Product[];

  return (
    <div className="space-y-6 md:space-y-8">
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 md:gap-4">
        <div className="bg-emerald-50 p-4 md:p-6 rounded-xl md:rounded-2xl border border-emerald-100 flex flex-col justify-between">
          <div>
            <p className="text-[10px] md:text-xs font-bold text-emerald-600 uppercase mb-1">System-Effizienz</p>
            <p className="text-2xl md:text-4xl font-bold text-emerald-700">{config.heatPump?.efficiency || '—'}</p>
          </div>
          <div className="mt-2 text-[10px] text-emerald-600/70 font-medium">Hervorragende Energieklasse</div>
        </div>
        <div className="bg-blue-50 p-4 md:p-6 rounded-xl md:rounded-2xl border border-blue-100 flex flex-col justify-between">
          <div>
            <p className="text-[10px] md:text-xs font-bold text-blue-600 uppercase mb-1">Heizleistung</p>
            <p className="text-2xl md:text-4xl font-bold text-blue-700">{config.heatPump?.power || '—'}</p>
          </div>
          <div className="mt-2 text-[10px] text-blue-600/70 font-medium">Optimale Wärmeverteilung</div>
        </div>
        <div className="bg-slate-900 p-4 md:p-6 rounded-xl md:rounded-2xl text-white shadow-lg flex flex-col justify-between">
          <div>
            <p className="text-[10px] md:text-xs font-bold text-slate-400 uppercase mb-1">Gesamtpreis (Netto)</p>
            <p className="text-2xl md:text-4xl font-mono font-bold text-[#A5CF4C]">
              {total.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
            </p>
          </div>
          <div className="mt-2 text-[10px] text-slate-400 font-medium">Zzgl. gesetzlicher MwSt.</div>
        </div>
      </div>

      <div className="bg-white rounded-xl md:rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
        <div className="bg-slate-50 px-4 py-4 md:px-6 border-b border-slate-200 flex justify-between items-center">
          <h3 className="text-base md:text-lg font-bold flex items-center gap-2 text-slate-800">
            <ShoppingCart size={18} md:size={20} className="text-[#A5CF4C]" />
            Gewählte Komponenten
          </h3>
          <span className="text-xs font-bold text-slate-500 bg-slate-200 px-2 py-1 rounded-full">
            {items.length} Positionen
          </span>
        </div>
        <div className="divide-y divide-slate-100">
          {items.map((item, idx) => (
            <div key={idx} className="flex justify-between items-start md:items-center p-4 md:px-6 hover:bg-slate-50 transition-colors gap-4">
              <div className="min-w-0">
                <div className="flex items-center gap-2 mb-0.5">
                  <span className="text-[10px] font-bold text-slate-400 w-4">{idx + 1}.</span>
                  <p className="font-bold text-slate-900 text-sm md:text-base truncate">{item.name}</p>
                </div>
                <p className="text-[10px] md:text-xs text-slate-500 ml-6">Art.-Nr: {item.articleNumber}</p>
              </div>
              <span className="font-mono font-bold text-sm md:text-base shrink-0 text-slate-700">
                {item.price.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
              </span>
            </div>
          ))}
        </div>
        <div className="bg-slate-50 p-4 md:p-6 border-t border-slate-200 flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-sm text-slate-500 text-center md:text-left">
            Überprüfen Sie Ihre Auswahl vor dem Abschluss. Alle Komponenten sind auf Kompatibilität geprüft.
          </div>
          <button 
            onClick={onPrint}
            className="w-full md:w-auto flex items-center justify-center gap-2 bg-[#A5CF4C] text-white px-6 py-3 rounded-xl font-bold hover:bg-[#94ba44] transition-all shadow-md active:scale-95"
          >
            <Download size={20} />
            <span>Als PDF speichern / Drucken</span>
          </button>
        </div>
      </div>
    </div>
  );
};

const InvoiceView: React.FC<{ config: Configuration, total: number }> = ({ config, total }) => {
  const items = [
    config.heatPump,
    config.storage,
    config.hydraulics,
    ...config.accessories,
    ...config.services
  ].filter(Boolean) as Product[];

  const date = new Date().toLocaleDateString('de-DE');

  return (
    <div className="bg-white min-h-screen p-6 md:p-12 text-slate-900 font-sans print:p-0">
      <div className="max-w-4xl mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-start mb-10 md:16 gap-6">
          <div>
            <div className="bg-[#A5CF4C] text-white px-4 py-2 md:px-6 md:py-3 rounded-lg font-bold text-2xl md:text-4xl tracking-tighter inline-block mb-4 md:mb-6">
              KERMI
            </div>
            <p className="text-slate-500 text-xs md:text-sm">
              Kermi GmbH<br />
              Pankofen-Bahnhof 1<br />
              94447 Plattling<br />
              Deutschland
            </p>
          </div>
          <div className="text-left md:text-right">
            <h1 className="text-xl md:text-3xl font-bold mb-1 md:mb-2">ANGEBOT / AUFTRAG</h1>
            <p className="text-slate-500 text-sm">Datum: {date}</p>
            <p className="text-slate-500 text-sm">Projekt: x-change WP System</p>
          </div>
        </div>

        <div className="mb-8 md:mb-12 overflow-x-auto">
          <h2 className="text-lg md:text-xl font-bold border-b-2 border-slate-900 pb-2 mb-4 md:mb-6">Zusammenstellung</h2>
          <table className="w-full min-w-[600px] md:min-w-0">
            <thead>
              <tr className="text-left text-[10px] md:text-xs font-bold uppercase text-slate-400 border-b border-slate-100">
                <th className="py-3 md:py-4">Pos.</th>
                <th className="py-3 md:py-4">Artikelnummer</th>
                <th className="py-3 md:py-4">Bezeichnung</th>
                <th className="py-3 md:py-4 text-right">Einzelpreis</th>
              </tr>
            </thead>
            <tbody>
              {items.map((item, idx) => (
                <tr key={idx} className="border-b border-slate-50">
                  <td className="py-3 md:py-4 text-sm">{idx + 1}</td>
                  <td className="py-3 md:py-4 font-mono text-xs md:text-sm">{item.articleNumber}</td>
                  <td className="py-3 md:py-4">
                    <p className="font-bold text-sm md:text-base">{item.name}</p>
                    <p className="text-[10px] md:text-xs text-slate-500">{item.description}</p>
                  </td>
                  <td className="py-3 md:py-4 text-right font-mono text-sm">
                    {item.price.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="flex justify-end">
          <div className="w-full md:w-64 space-y-2 md:space-y-3">
            <div className="flex justify-between text-slate-500 text-sm">
              <span>Zwischensumme:</span>
              <span className="font-mono">{total.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}</span>
            </div>
            <div className="flex justify-between text-slate-500 text-sm">
              <span>MwSt. (19%):</span>
              <span className="font-mono">{(total * 0.19).toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}</span>
            </div>
            <div className="flex justify-between text-xl md:text-2xl font-bold pt-3 md:pt-4 border-t-2 border-slate-900">
              <span>Gesamt:</span>
              <span className="text-[#A5CF4C]">
                {(total * 1.19).toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
              </span>
            </div>
          </div>
        </div>

        <div className="mt-16 md:mt-24 pt-8 md:pt-12 border-t border-slate-100 text-center text-[10px] md:text-xs text-slate-400 space-y-1 md:space-y-2">
          <p>Dieses Dokument wurde automatisch erstellt und ist ohne Unterschrift gültig.</p>
          <p>Kermi GmbH | Pankofen-Bahnhof 1 | 94447 Plattling | www.kermi.de</p>
        </div>
      </div>
    </div>
  );
};

export default function App() {
  const [currentStep, setCurrentStep] = useState(0);
  const [config, setConfig] = useState<Configuration>({
    accessories: [],
    services: [],
  });
  const [isPrinting, setIsPrinting] = useState(false);

  const totalCost = useMemo(() => {
    let total = 0;
    if (config.heatPump) total += config.heatPump.price;
    if (config.storage) total += config.storage.price;
    if (config.hydraulics) total += config.hydraulics.price;
    total += config.accessories.reduce((sum, item) => sum + item.price, 0);
    total += config.services.reduce((sum, item) => sum + item.price, 0);
    return total;
  }, [config]);

  const handleSelectHeatPump = (hp: Product) => {
    setConfig(prev => ({
      ...prev,
      heatPump: hp,
      // Reset incompatible items
      storage: prev.storage && isCompatible(hp, prev.storage) ? prev.storage : undefined,
      hydraulics: prev.hydraulics && isCompatible(hp, prev.hydraulics) ? prev.hydraulics : undefined,
    }));
  };

  const handleSelectStorage = (storage: Product) => {
    setConfig(prev => ({ 
      ...prev, 
      storage,
      // If x-buffer combi pro is selected, clear hydraulics as it's already included
      hydraulics: storage.articleNumber === 'W30295' ? undefined : prev.hydraulics
    }));
  };

  const handleSelectHydraulics = (hydro: Product) => {
    setConfig(prev => ({ ...prev, hydraulics: hydro }));
  };

  const isHydraulicsDisabled = config.storage?.articleNumber === 'W30295';

  const toggleAccessory = (acc: Product) => {
    setConfig(prev => {
      const exists = prev.accessories.find(a => a.id === acc.id);
      if (exists) {
        return { ...prev, accessories: prev.accessories.filter(a => a.id !== acc.id) };
      }
      return { ...prev, accessories: [...prev.accessories, acc] };
    });
  };

  const toggleService = (srv: Product) => {
    setConfig(prev => {
      const exists = prev.services.find(s => s.id === srv.id);
      if (exists) {
        return { ...prev, services: prev.services.filter(s => s.id !== srv.id) };
      }
      return { ...prev, services: [...prev.services, srv] };
    });
  };

  const isCompatible = (hp: Product | undefined, item: Product) => {
    if (!hp) return true;
    if (!item.compatibleWith) return true;
    // Check if item's article number is in HP's compatibility list OR vice versa
    const hpCompat = hp.compatibleWith || [];
    const itemCompat = item.compatibleWith || [];
    return hpCompat.includes(item.articleNumber) || itemCompat.includes(hp.articleNumber) || (hpCompat.length === 0 && itemCompat.length === 0);
  };

  const nextStep = () => setCurrentStep(prev => Math.min(prev + 1, STEPS.length - 1));
  const prevStep = () => setCurrentStep(prev => Math.max(prev - 1, 0));

  const handlePrint = () => {
    setIsPrinting(true);
    setTimeout(() => {
      window.print();
      setIsPrinting(false);
    }, 500);
  };

  if (isPrinting) {
    return <InvoiceView config={config} total={totalCost} />;
  }

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-900 pb-24 md:pb-0">
      {/* Header */}
      <header className="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 h-16 md:h-20 flex items-center justify-between">
          <div className="flex items-center gap-2 md:gap-4">
            <div className="bg-[#A5CF4C] text-white px-3 py-1.5 md:px-4 md:py-2 rounded-lg font-bold text-lg md:text-2xl tracking-tighter">
              KERMI
            </div>
            <div className="h-6 md:h-8 w-px bg-slate-200 hidden sm:block" />
            <h1 className="text-sm md:text-xl font-semibold text-slate-700 truncate max-w-[120px] sm:max-w-none">x-change Konfigurator</h1>
          </div>
          <div className="flex items-center gap-3 md:gap-6">
            <div className="text-right hidden sm:block">
              <p className="text-[10px] md:text-xs text-slate-500 uppercase font-bold tracking-wider">Gesamt</p>
              <p className="text-sm md:text-2xl font-mono font-bold text-[#A5CF4C]">
                {totalCost.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' })}
              </p>
            </div>
            <button 
              onClick={handlePrint}
              className="flex items-center gap-2 bg-[#A5CF4C] text-white px-4 py-2 md:px-5 md:py-2.5 rounded-xl hover:bg-[#94ba44] transition-all shadow-md active:scale-95"
              title="Als PDF speichern / Drucken"
            >
              <Download size={18} />
              <span className="hidden md:inline font-bold">PDF / Drucken</span>
            </button>
          </div>
        </div>
      </header>

      {/* Mobile Step Indicator */}
      <div className="md:hidden bg-white border-b border-slate-200 overflow-x-auto no-scrollbar sticky top-16 z-40">
        <div className="flex px-4 py-3 gap-2 min-w-max">
          {STEPS.map((step, idx) => {
            const Icon = step.icon;
            const isActive = currentStep === idx;
            const isCompleted = currentStep > idx;
            const isDisabledStep = step.id === 'hydraulics' && isHydraulicsDisabled;
            
            return (
              <button
                key={step.id}
                disabled={isDisabledStep}
                onClick={() => !isDisabledStep && setCurrentStep(idx)}
                className={`flex items-center gap-2 px-3 py-2 rounded-lg transition-all ${
                  isDisabledStep ? 'opacity-20 grayscale' :
                  isActive ? 'bg-[#A5CF4C] text-white shadow-sm' : 'bg-slate-100 text-slate-500'
                }`}
              >
                <Icon size={16} />
                <span className="text-xs font-bold whitespace-nowrap">{step.label}</span>
                {isCompleted && !isActive && <CheckCircle2 size={12} className="text-emerald-500" />}
              </button>
            );
          })}
        </div>
      </div>

      <main className="max-w-7xl mx-auto px-4 py-6 md:py-8 flex flex-col md:flex-row gap-8">
        {/* Desktop Sidebar Navigation */}
        <aside className="hidden md:block w-64 shrink-0">
          <nav className="space-y-1">
            {STEPS.map((step, idx) => {
              const Icon = step.icon;
              const isActive = currentStep === idx;
              const isCompleted = currentStep > idx;
              const isDisabledStep = step.id === 'hydraulics' && isHydraulicsDisabled;
              return (
                <button
                  key={step.id}
                  disabled={isDisabledStep}
                  onClick={() => !isDisabledStep && setCurrentStep(idx)}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${
                    isDisabledStep ? 'opacity-30 cursor-not-allowed' :
                    isActive 
                      ? 'bg-white shadow-md text-[#A5CF4C] ring-1 ring-slate-200' 
                      : 'text-slate-500 hover:bg-slate-100'
                  }`}
                >
                  <div className={`p-2 rounded-lg ${isActive ? 'bg-[#A5CF4C]/10' : 'bg-slate-100'}`}>
                    <Icon size={20} />
                  </div>
                  <span className="font-medium text-sm">{step.label}</span>
                  {isCompleted && <CheckCircle2 size={16} className="ml-auto text-emerald-500" />}
                  {isDisabledStep && <AlertCircle size={16} className="ml-auto text-amber-500" />}
                </button>
              );
            })}
          </nav>

          {/* Mini Summary */}
          <div className="mt-8 p-6 bg-slate-900 rounded-2xl text-white shadow-xl">
            <h3 className="text-xs font-bold uppercase tracking-widest text-slate-400 mb-4">Aktuelle Auswahl</h3>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between gap-2">
                <span className="text-slate-400">WP:</span>
                <span className="text-right font-medium truncate">{config.heatPump?.name || '—'}</span>
              </div>
              <div className="flex justify-between gap-2">
                <span className="text-slate-400">Speicher:</span>
                <span className="text-right font-medium truncate">{config.storage?.name || '—'}</span>
              </div>
              <div className="flex justify-between gap-2">
                <span className="text-slate-400">Hydraulik:</span>
                <span className="text-right font-medium truncate">{config.hydraulics?.name || '—'}</span>
              </div>
            </div>
          </div>
        </aside>

        {/* Content Area */}
        <div className="flex-1 min-w-0">
          <AnimatePresence mode="wait">
            <motion.div
              key={currentStep}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className="bg-white rounded-2xl md:rounded-3xl shadow-sm border border-slate-200 p-5 md:p-8 min-h-[500px] md:min-h-[600px] flex flex-col"
            >
              <div className="mb-6 md:mb-8">
                <h2 className="text-2xl md:text-3xl font-bold text-slate-900 mb-1 md:mb-2">{STEPS[currentStep].label}</h2>
                <p className="text-sm md:text-base text-slate-500">Wählen Sie die passende Komponente für Ihr System.</p>
              </div>

              <div className="flex-1">
                {currentStep === 0 && (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {PRODUCTS.filter(p => p.category === 'heatpump').map(hp => (
                      <ProductCard 
                        key={hp.id} 
                        product={hp} 
                        isSelected={!!config.heatPump && config.heatPump.id === hp.id}
                        onSelect={() => handleSelectHeatPump(hp)}
                      />
                    ))}
                  </div>
                )}

                {currentStep === 1 && (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {PRODUCTS.filter(p => p.category === 'storage').map(st => (
                      <ProductCard 
                        key={st.id} 
                        product={st} 
                        isSelected={!!config.storage && config.storage.id === st.id}
                        isDisabled={!isCompatible(config.heatPump, st)}
                        onSelect={() => handleSelectStorage(st)}
                      />
                    ))}
                  </div>
                )}

                {currentStep === 2 && (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {isHydraulicsDisabled ? (
                      <div className="col-span-full p-8 md:p-12 text-center bg-slate-50 rounded-2xl md:rounded-3xl border-2 border-dashed border-slate-200">
                        <Info className="mx-auto text-slate-400 mb-4" size={40} md:size={48} />
                        <h3 className="text-lg font-bold text-slate-600 mb-2">Nicht erforderlich</h3>
                        <p className="text-sm md:text-base text-slate-500 max-w-md mx-auto">
                          Da Sie den <span className="font-bold text-slate-700">x-buffer combi pro</span> gewählt haben, 
                          ist die Hydraulik und Regelung bereits im Speicher integriert.
                        </p>
                      </div>
                    ) : (
                      PRODUCTS.filter(p => p.category === 'hydraulics').map(hy => (
                        <ProductCard 
                          key={hy.id} 
                          product={hy} 
                          isSelected={!!config.hydraulics && config.hydraulics.id === hy.id}
                          isDisabled={!isCompatible(config.heatPump, hy)}
                          onSelect={() => handleSelectHydraulics(hy)}
                        />
                      ))
                    )}
                  </div>
                )}

                {currentStep === 3 && (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {PRODUCTS.filter(p => p.category === 'accessory').map(acc => (
                      <ProductCard 
                        key={acc.id} 
                        product={acc} 
                        isSelected={config.accessories.some(a => a.id === acc.id)}
                        onSelect={() => toggleAccessory(acc)}
                        isMulti
                      />
                    ))}
                  </div>
                )}

                {currentStep === 4 && (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {PRODUCTS.filter(p => p.category === 'service').map(srv => (
                      <ProductCard 
                        key={srv.id} 
                        product={srv} 
                        isSelected={config.services.some(s => s.id === srv.id)}
                        onSelect={() => toggleService(srv)}
                        isMulti
                      />
                    ))}
                  </div>
                )}

                {currentStep === 5 && (
                  <SummaryView config={config} total={totalCost} onPrint={handlePrint} />
                )}
              </div>

              {/* Desktop Footer Controls */}
              <div className="hidden md:flex mt-12 pt-8 border-t border-slate-100 justify-between">
                <button
                  onClick={prevStep}
                  disabled={currentStep === 0}
                  className="flex items-center gap-2 px-6 py-3 rounded-xl font-semibold text-slate-600 hover:bg-slate-50 disabled:opacity-30 transition-all"
                >
                  <ChevronLeft size={20} />
                  <span>Zurück</span>
                </button>
                <button
                  onClick={nextStep}
                  disabled={currentStep === STEPS.length - 1}
                  className="flex items-center gap-2 bg-[#A5CF4C] text-white px-8 py-3 rounded-xl font-bold shadow-lg shadow-[#A5CF4C]/20 hover:scale-[1.02] active:scale-[0.98] transition-all disabled:opacity-30"
                >
                  <span>Weiter</span>
                  <ChevronRight size={20} />
                </button>
              </div>
            </motion.div>
          </AnimatePresence>
        </div>
      </main>

      {/* Mobile Sticky Footer Controls */}
      <div className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-4 flex gap-3 z-50 shadow-[0_-4px_20px_rgba(0,0,0,0.05)]">
        <button
          onClick={prevStep}
          disabled={currentStep === 0}
          className="flex-1 flex items-center justify-center gap-2 py-3 rounded-xl font-bold text-slate-600 bg-slate-100 disabled:opacity-30"
        >
          <ChevronLeft size={18} />
          <span>Zurück</span>
        </button>
        <button
          onClick={nextStep}
          disabled={currentStep === STEPS.length - 1}
          className="flex-[2] flex items-center justify-center gap-2 bg-[#A5CF4C] text-white py-3 rounded-xl font-bold shadow-lg shadow-[#A5CF4C]/20 disabled:opacity-30"
        >
          <span>{currentStep === STEPS.length - 1 ? 'Fertig' : 'Weiter'}</span>
          <ChevronRight size={18} />
        </button>
      </div>
    </div>
  );
}


