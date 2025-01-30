import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DashboardLayout from './components/layout/dashboardlayaout.tsx';
import Dashboard from './pages/dashboard.tsx';
import Estudiantes from './pages/estudiantes.tsx';
import Atrasos from './pages/atrasos.tsx';
import Reportes from './pages/reportes.tsx';
import Notificaciones from './pages/notificaciones.tsx';

function App() {
  return (
  <Router>
    <DashboardLayout>
      <Routes>
        <Route path='/' element={<Dashboard />} />
        <Route path='/estudiantes' element={<Estudiantes />} />
        <Route path='/atrasos' element={<Atrasos />} />
        <Route path='/reportes' element={<Reportes />} />
        <Route path='/notificaciones' element={<Notificaciones />} />
      </Routes>
    </DashboardLayout>
  </Router>  
  )
}

export default App