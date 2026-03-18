import { useState, useEffect } from 'react';

export default function ProfileCalculator() {
  const [formData, setFormData] = useState({
    f_id: false, f_em_id: false, f_em_reach: false,
    f_mo_id: false, f_mo_reach: false, f_pu: false,
    f_act: 0, f_eng: 0
  });

  const [result, setResult] = useState({ active: false, archived: false, type: "Anonymous", limit: 60 });

  const syncInputs = (type, source) => {
    const newVal = !formData[`f_${type}_${source}`];
    setFormData(prev => ({
      ...prev,
      [`f_${type}_id`]: newVal,
      [`f_${type}_reach`]: newVal
    }));
  };

  useEffect(() => {
    const { f_id, f_em_id, f_mo_id, f_pu, f_act, f_eng } = formData;
    const active = f_id || f_em_id || f_mo_id || f_pu || f_act > 0 || f_eng > 0;
    const reachable = f_em_id || f_mo_id || f_pu;
    const registered = f_id && (f_em_id || f_mo_id);
    const limit = registered ? 365 : 60;
    const archived = !reachable && (f_act > limit) && (f_eng > limit);

    setResult({ active, archived, type: registered ? "Registered" : "Anonymous", limit });
  }, [formData]);

  const resetAll = () => setFormData({
    f_id: false, f_em_id: false, f_em_reach: false,
    f_mo_id: false, f_mo_reach: false, f_pu: false,
    f_act: 0, f_eng: 0
  });

  return (
    <div style={{ fontFamily: 'Inter, Arial, sans-serif', border: '1px solid #e1e8ed', borderRadius: '12px', background: '#fff', maxWidth: '950px', margin: '20px auto', overflow: 'hidden' }}>
      <div style={{ background: '#023047', color: 'white', padding: '12px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: '13px', fontWeight: 'bold', textTransform: 'uppercase' }}>Profile Retention Calculator</span>
        <button style={{ background: 'rgba(255,255,255,0.2)', border: '1px solid rgba(255,255,255,0.3)', color: 'white', fontSize: '10px', padding: '4px 8px', borderRadius: '4px', cursor: 'pointer' }} onClick={resetAll}>RESET</button>
      </div>
      <div style={{ display: 'flex', flexWrap: 'wrap', background: '#e1e8ed' }}>
        <div style={{ flex: '1.5', minWidth: '350px', display: 'flex', flexDirection: 'column', gap: '1px' }}>
          <div style={{ background: '#fff', padding: '20px' }}>
            <div style={{ fontSize: '11px', fontWeight: '800', color: '#6a7c92', textTransform: 'uppercase', marginBottom: '12px' }}>1. User Type & Reachability</div>
            <div style={{ display: 'flex', gap: '8px', marginBottom: '12px' }}>
              {['f_id', 'f_em_id', 'f_mo_id'].map(id => (
                <label key={id} style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                  <input type="checkbox" checked={formData[id]} onChange={() => id === 'f_id' ? setFormData(p => ({...p, f_id: !p.f_id})) : syncInputs(id.split('_')[1], 'id')} style={{ marginRight: '8px' }} /> 
                  {id === 'f_id' ? 'ID' : id === 'f_em_id' ? 'Email ID' : 'Mobile No.'}
                </label>
              ))}
            </div>
            {/* ... Repeat for Reachability across channels, Activity, and Engagement ... */}
          </div>
        </div>
        <div style={{ flex: '1', minWidth: '280px', background: '#f8fafc', padding: '30px', borderLeft: '1px solid #e1e8ed', textAlign: 'center' }}>
          {!result.active ? (
            <div style={{ color: '#6a7c92', fontSize: '14px', fontStyle: 'italic' }}>Enter user criteria to evaluate archival status</div>
          ) : (
            <div>
              <div style={{ 
                background: result.archived ? "#fdeaea" : "#e6f7f4", 
                color: result.archived ? "#d90429" : "#2a9d8f",
                border: `1px solid ${result.archived ? "#d90429" : "#2a9d8f"}`,
                padding: '10px 0', borderRadius: '50px', fontSize: '20px', fontWeight: '800', marginBottom: '20px'
              }}>
                {result.archived ? "ARCHIVE" : "RETAIN"}
              </div>
              <div style={{ background: '#fff', border: '1px solid #e1e8ed', borderRadius: '8px', padding: '16px', textAlign: 'left' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 'bold', color: '#6a7c92' }}>CLASSIFICATION</span>
                  <span style={{ fontSize: '13px', fontWeight: 'bold' }}>{result.type} ({result.limit}d)</span>
                </div>
                <div style={{ fontSize: '13px', color: '#475569' }}>
                   {result.archived ? "Archival Triggered: Unreachable and inactivity limits exceeded." : "Safe: User is reachable or within activity window."}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}