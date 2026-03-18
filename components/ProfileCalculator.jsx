import React, { useState, useEffect } from 'react';

const ProfileCalculator = () => {
  const [inputs, setInputs] = useState({
    f_id: false, f_em_id: false, f_mo_id: false,
    f_em_reach: false, f_mo_reach: false, f_pu: false,
    f_act: 0, f_eng: 0
  });

  const [display, setDisplay] = useState({ active: false, archived: false, type: 'Anonymous', limit: 60 });

  const sync = (type, source) => {
    const newVal = !inputs[`f_${type}_${source}`];
    setInputs(prev => ({ ...prev, [`f_${type}_id`]: newVal, [`f_${type}_reach`]: newVal }));
  };

  useEffect(() => {
    const { f_id, f_em_id, f_mo_id, f_pu, f_act, f_eng } = inputs;
    const isActive = f_id || f_em_id || f_mo_id || f_pu || f_act > 0 || f_eng > 0;
    const reachable = f_em_id || f_mo_id || f_pu;
    const registered = f_id && (f_em_id || f_mo_id);
    const limit = registered ? 365 : 60;
    const isArchived = !reachable && (f_act > limit) && (f_eng > limit);

    setDisplay({ active: isActive, archived: isArchived, type: registered ? 'Registered' : 'Anonymous', limit });
  }, [inputs]);

  return (
    <div style={{ fontFamily: 'Inter, sans-serif', border: '1px solid #e1e8ed', borderRadius: '12px', background: '#fff', maxWidth: '950px', margin: '20px auto', overflow: 'hidden' }}>
      <div style={{ background: '#023047', color: 'white', padding: '12px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: '13px', fontWeight: 'bold', textTransform: 'uppercase' }}>Profile Retention Calculator</span>
        <button onClick={() => setInputs({ f_id: false, f_em_id: false, f_mo_id: false, f_em_reach: false, f_mo_reach: false, f_pu: false, f_act: 0, f_eng: 0 })} style={{ background: 'rgba(255,255,255,0.2)', border: '1px solid rgba(255,255,255,0.3)', color: 'white', fontSize: '10px', padding: '4px 8px', borderRadius: '4px', cursor: 'pointer' }}>RESET</button>
      </div>
      
      <div style={{ display: 'flex', flexWrap: 'wrap', background: '#e1e8ed', gap: '1px' }}>
        <div style={{ flex: '1.5', minWidth: '350px', background: '#e1e8ed', display: 'flex', flexDirection: 'column', gap: '1px' }}>
          {/* Section 1: User Type */}
          <div style={{ background: '#fff', padding: '20px' }}>
            <div style={{ fontSize: '11px', fontWeight: '800', color: '#6a7c92', textTransform: 'uppercase', marginBottom: '12px' }}>1. User Type & Reachability</div>
            <div style={{ display: 'flex', gap: '8px', marginBottom: '12px' }}>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_id} onChange={() => setInputs(p => ({...p, f_id: !p.f_id}))} style={{marginRight: '8px'}} /> ID
              </label>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_em_id} onChange={() => sync('em', 'id')} style={{marginRight: '8px'}} /> Email ID
              </label>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_mo_id} onChange={() => sync('mo', 'id')} style={{marginRight: '8px'}} /> Mobile No.
              </label>
            </div>
            <div style={{ display: 'flex', gap: '8px' }}>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_em_reach} onChange={() => sync('em', 'reach')} style={{marginRight: '8px'}} /> Email
              </label>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_mo_reach} onChange={() => sync('mo', 'reach')} style={{marginRight: '8px'}} /> SMS
              </label>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', fontSize: '12px', border: '1px solid #e1e8ed', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
                <input type="checkbox" checked={inputs.f_pu} onChange={() => setInputs(p => ({...p, f_pu: !p.f_pu}))} style={{marginRight: '8px'}} /> Push
              </label>
            </div>
          </div>

          {/* Section 2: Activity */}
          <div style={{ background: '#fff', padding: '20px' }}>
            <div style={{ fontSize: '11px', fontWeight: '800', color: '#6a7c92', textTransform: 'uppercase', marginBottom: '8px' }}>2. Activity</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
              <input type="number" value={inputs.f_act} onChange={(e) => setInputs(p => ({...p, f_act: parseInt(e.target.value) || 0}))} style={{ width: '80px', padding: '10px', border: '1px solid #e1e8ed', borderRadius: '6px', fontSize: '18px', fontWeight: 'bold' }} />
              <span style={{ fontSize: '12px', color: '#6a7c92' }}>Days since last brand interaction (events)</span>
            </div>
          </div>

          {/* Section 3: Campaign Engagement */}
          <div style={{ background: '#fff', padding: '20px' }}>
            <div style={{ fontSize: '11px', fontWeight: '800', color: '#6a7c92', textTransform: 'uppercase', marginBottom: '8px' }}>3. Campaign Engagement</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
              <input type="number" value={inputs.f_eng} onChange={(e) => setInputs(p => ({...p, f_eng: parseInt(e.target.value) || 0}))} style={{ width: '80px', padding: '10px', border: '1px solid #e1e8ed', borderRadius: '6px', fontSize: '18px', fontWeight: 'bold' }} />
              <span style={{ fontSize: '12px', color: '#6a7c92' }}>Days since interaction with campaigns</span>
            </div>
          </div>
        </div>

        {/* Right Side: Result Display */}
        <div style={{ flex: '1', minWidth: '280px', background: '#f8fafc', padding: '30px', display: 'flex', flexDirection: 'column', justifyContent: 'center', borderLeft: '1px solid #e1e8ed' }}>
          {!display.active ? (
            <div style={{ color: '#6a7c92', fontSize: '14px', fontStyle: 'italic', textAlign: 'center' }}>Enter user criteria to evaluate archival status</div>
          ) : (
            <div style={{ width: '100%' }}>
              <div style={{ 
                textAlign: 'center', padding: '10px 0', borderRadius: '50px', fontSize: '20px', fontWeight: '800', marginBottom: '20px',
                background: display.archived ? '#fdeaea' : '#e6f7f4', 
                color: display.archived ? '#d90429' : '#2a9d8f',
                border: `1px solid ${display.archived ? '#d90429' : '#2a9d8f'}`
              }}>
                {display.archived ? 'ARCHIVE' : 'RETAIN'}
              </div>
              <div style={{ background: '#fff', border: '1px solid #e1e8ed', borderRadius: '8px', padding: '16px', borderLeft: '4px solid #023047' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px', borderBottom: '1px solid #f1f5f9', paddingBottom: '8px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 'bold', color: '#6a7c92' }}>USER CLASSIFICATION</span>
                  <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#023047' }}>{display.type} ({display.limit}d Limit)</span>
                </div>
                <div style={{ fontSize: '13px', color: '#475569', lineHeight: '1.5' }}>
                  {display.archived ? <b>Status: Archival Triggered.</b> : <b>Status: Safe.</b>} {display.archived ? 'Unreachable and inactivity limits exceeded.' : 'Profile is within retention window.'}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProfileCalculator;