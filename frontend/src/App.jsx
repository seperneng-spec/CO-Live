import React from 'react';

import ControlPanel from './components/ControlPanel';
import SpeechOverlay from './components/SpeechOverlay';
import ThreeViewer from './components/ThreeViewer';

import './index.css';

export default function App() {
  return (
    <div className="app-shell">
      <header>
        <h1>CO-Live Studio</h1>
      </header>
      <main className="studio-layout">
        <ControlPanel />
        <ThreeViewer />
        <SpeechOverlay />
      </main>
    </div>
  );
}
