import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  LayoutDashboard,
  Users,
  ClipboardList,
  Bell,
  MessageCircle,
  FileText,
  Calendar,
  Settings,
  LogOut,
  ChevronLeft,
  ChevronRight
} from "lucide-react"
import { Link } from 'react-router-dom'

export const Sidebar = () => {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)

  const toggleSidebar = () => setSidebarCollapsed(!sidebarCollapsed)

  const menuItems = [
    { icon: <LayoutDashboard size={24} />, label: 'Dashboard', path: '/' },
    { icon: <Users size={24} />, label: 'Students', path: '/estudiantes' },
    { icon: <ClipboardList size={24} />, label: 'Attendance', path: '/atrasos' },
    { icon: <Bell size={24} />, label: 'Notifications', path: '/notificaciones' },
    { icon: <MessageCircle size={24} />, label: 'Messages', path: '/mensajes' },
    { icon: <FileText size={24} />, label: 'Reports', path: '/reportes' },
    { icon: <Calendar size={24} />, label: 'Schedule', path: '/horarios' },
    { icon: <Settings size={24} />, label: 'Settings', path: '/configuracion' },
  ]

  return (
    <aside className={`bg-white ${sidebarCollapsed ? 'w-16' : 'w-64'} transition-all duration-300 ease-in-out`}>
      <div className="flex flex-col h-full">
        <div className="flex items-center justify-between p-4 border-b">
          {!sidebarCollapsed && <h2 className="text-xl font-bold">Admin Panel</h2>}
          <Button variant="ghost" size="icon" onClick={toggleSidebar}>
            {sidebarCollapsed ? <ChevronRight /> : <ChevronLeft />}
          </Button>
        </div>
        <ScrollArea className="flex-grow">
          <nav className="space-y-2 p-2">
            {menuItems.map((item, index) => (
              <Link key={index} to={item.path}>
                <Button variant="ghost" className="w-full justify-start">
                  {item.icon}
                  {!sidebarCollapsed && <span className="ml-2">{item.label}</span>}
                </Button>
              </Link>
            ))}
          </nav>
        </ScrollArea>
        <div className="p-4 border-t">
          <Button variant="ghost" className="w-full justify-start">
            <LogOut size={24} />
            {!sidebarCollapsed && <span className="ml-2">Logout</span>}
          </Button>
        </div>
      </div>
    </aside>
  )
}