import { useState, useRef } from 'react'
import './index.css'

function App() {
  const [diseaseName, setDiseaseName] = useState('')
  const [description, setDescription] = useState('')
  const [fileName, setFileName] = useState('')
  const [toast, setToast] = useState(false)
  const fileRef = useRef()

  const handleFile = (e) => {
    if (e.target.files[0]) setFileName(e.target.files[0].name)
  }

  const handleForward = () => {
    if (!diseaseName.trim() || !description.trim()) {
      alert('Please fill in both disease name and patient description.')
      return
    }
    setToast(true)
    setTimeout(() => setToast(false), 3000)
  }

  return (
    <div className="page-wrapper">
      <div className="form-card">

        <div className="form-header">
          <h2 className="form-title">Patient Information</h2>
          <p className="form-subtitle">Fill in the details below and forward to the medical team</p>
        </div>

        <div className="field-group">
          <label className="field-label" htmlFor="disease-name">Disease Name</label>
          <input
            id="disease-name"
            type="text"
            className="field-input"
            value={diseaseName}
            onChange={e => setDiseaseName(e.target.value)}
            placeholder="e.g. Type 2 Diabetes, Hypertension"
          />
        </div>

        <div className="field-group">
          <label className="field-label" htmlFor="description">Description about the Patient</label>
          <textarea
            id="description"
            className="field-textarea"
            value={description}
            onChange={e => setDescription(e.target.value)}
            placeholder="Describe the patient's condition, symptoms, history..."
            rows={4}
          />
        </div>

        <div className="field-group">
          <label className="field-label">Patient Report</label>
          <div className="upload-zone" onClick={() => fileRef.current.click()}>
            <input
              type="file"
              ref={fileRef}
              className="file-input-hidden"
              onChange={handleFile}
              accept=".pdf,.doc,.docx,.png,.jpg,.jpeg"
            />
            <p className="upload-icon">📎</p>
            <p className="upload-label">Click to upload report</p>
            <p className="upload-hint">PDF, DOC, DOCX, PNG, JPG up to 10MB</p>
            {fileName && <p className="file-name-display">{fileName}</p>}
          </div>
        </div>

        <button className="forward-btn" onClick={handleForward}>
          Forward Message
        </button>

        {toast && (
          <div className="toast-success">
            ✅ Message forwarded successfully!
          </div>
        )}

      </div>
    </div>
  )
}

export default App