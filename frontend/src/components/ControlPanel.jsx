import React from 'react';

export default function ControlPanel() {
  return (
    <aside className="control-panel">
      <h2>Control Panel</h2>
      <button type="button">Start Stream</button>
      <button type="button">Stop Stream</button>
      <button type="button">Trigger Mood</button>
    </aside>
  );
}
