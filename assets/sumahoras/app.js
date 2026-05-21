const GRADOS_DEFAULT = [
    "Agente", "Cabo", "Cabo 1", "Sargento", "Sargento 1", "Sargento Ayudante", 
    "Suboficial Principal", "Suboficial Mayor", "SUBADJUTOR", "ADJUTOR", 
    "ADJUTOR MAYOR", "SUBALCAIDE", "ALCAIDE", "ALCAIDE MAYOR", "SUPREFECTO", 
    "PREFECTO", "PREFECTO MAYOR", "contratado"
];

const UNIDADES_DEFAULT = ["IEA1", "IEA2", "IEA3", "IEA4", "IEMT", "IEAHT", "IEAT", "PJPJ"];

class App {
    constructor() {
        this.data = {
            personal: [],
            unidades: [],
            horas: []
        };
        this.currentPersonalId = null;
        this.currentDate = new Date();
        this.init();
    }

    init() {
        this.loadData();
        this.cacheDOM();
        this.bindEvents();
        this.renderUnidades();
        this.renderPersonal();
    }

    loadData() {
        const stored = localStorage.getItem('sumahoras_data');
        if (stored) {
            this.data = JSON.parse(stored);
        }
        
        if (!this.data.unidades || this.data.unidades.length === 0) {
            this.data.unidades = [...UNIDADES_DEFAULT];
            this.saveData();
        }
    }

    saveData() {
        localStorage.setItem('sumahoras_data', JSON.stringify(this.data));
    }

    cacheDOM() {
        // Nav
        this.navItems = document.querySelectorAll('.nav-item');
        this.views = document.querySelectorAll('.view');
        
        // Modals
        this.modalPersonal = document.getElementById('modal-personal');
        this.modalHoras = document.getElementById('modal-horas');
        this.modalSync = document.getElementById('modal-sync');
        
        // Forms
        this.formPersonal = document.getElementById('form-personal');
        this.formAddHora = document.getElementById('form-add-hora');
        
        // Lists
        this.personalList = document.getElementById('personal-list');
        this.unidadesList = document.getElementById('unidades-list');
        this.horasList = document.getElementById('horas-list');
        
        // Search
        this.searchPersonal = document.getElementById('search-personal');
        
        // Month Selector
        this.monthSelector = document.getElementById('horas-month-selector');
        this.monthDisplay = document.getElementById('current-month-display');
        
        // Sync
        this.importFile = document.getElementById('import-file');
    }

    bindEvents() {
        // Navigation
        this.navItems.forEach(item => {
            item.addEventListener('click', (e) => {
                this.navItems.forEach(n => n.classList.remove('active'));
                item.classList.add('active');
                this.views.forEach(v => v.classList.remove('active'));
                document.getElementById(item.dataset.target).classList.add('active');
            });
        });

        // Close Modals
        document.querySelectorAll('.close-modal').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.target.closest('.modal').classList.remove('show');
            });
        });

        // Forms
        this.formPersonal.addEventListener('submit', this.handlePersonalSubmit.bind(this));
        this.formAddHora.addEventListener('submit', this.handleAddHora.bind(this));

        // Search
        this.searchPersonal.addEventListener('input', this.renderPersonal.bind(this));

        // Month Selector
        document.getElementById('prev-month').addEventListener('click', () => this.changeMonth(-1));
        document.getElementById('next-month').addEventListener('click', () => this.changeMonth(1));
        this.monthSelector.addEventListener('change', (e) => {
            if(e.target.value) {
                const parts = e.target.value.split('-');
                this.currentDate = new Date(parts[0], parts[1] - 1, 1);
                this.updateMonthView();
            }
        });
        
        // Sync
        document.getElementById('btn-export-import').addEventListener('click', () => {
            this.modalSync.classList.add('show');
        });
        this.importFile.addEventListener('change', this.importData.bind(this));
    }

    // --- PERSONAL MANAGEMENT ---
    
    showAddPersonalModal(id = null) {
        const title = document.getElementById('modal-personal-title');
        const gradoSelect = document.getElementById('personal-grado');
        const unidadSelect = document.getElementById('personal-unidad');
        
        // Populate Selects
        gradoSelect.innerHTML = GRADOS_DEFAULT.map(g => `<option value="${g}">${g}</option>`).join('');
        unidadSelect.innerHTML = this.data.unidades.map(u => `<option value="${u}">${u}</option>`).join('');
        
        if (id) {
            title.textContent = 'Editar Personal';
            const person = this.data.personal.find(p => p.id === id);
            document.getElementById('personal-id').value = person.id;
            document.getElementById('personal-legajo').value = person.legajo;
            document.getElementById('personal-grado').value = person.grado;
            document.getElementById('personal-nombre').value = person.nombre;
            document.getElementById('personal-unidad').value = person.unidad;
        } else {
            title.textContent = 'Agregar Personal';
            this.formPersonal.reset();
            document.getElementById('personal-id').value = '';
        }
        
        this.modalPersonal.classList.add('show');
    }

    handlePersonalSubmit(e) {
        e.preventDefault();
        const id = document.getElementById('personal-id').value;
        const legajo = document.getElementById('personal-legajo').value.trim();
        const grado = document.getElementById('personal-grado').value;
        const nombre = document.getElementById('personal-nombre').value.trim();
        const unidad = document.getElementById('personal-unidad').value;
        
        if (id) {
            // Edit
            const index = this.data.personal.findIndex(p => p.id == id);
            if(index !== -1) {
                this.data.personal[index] = { ...this.data.personal[index], legajo, grado, nombre, unidad };
            }
        } else {
            // Add
            this.data.personal.push({
                id: Date.now().toString(),
                legajo, grado, nombre, unidad
            });
        }
        
        this.saveData();
        this.renderPersonal();
        this.modalPersonal.classList.remove('show');
    }

    deletePersonal(id) {
        if(confirm('¿Seguro que deseas eliminar este personal y todas sus horas?')) {
            this.data.personal = this.data.personal.filter(p => p.id !== id);
            this.data.horas = this.data.horas.filter(h => h.personalId !== id);
            this.saveData();
            this.renderPersonal();
        }
    }

    renderPersonal() {
        const term = this.searchPersonal.value.toLowerCase();
        const filtered = this.data.personal.filter(p => 
            p.nombre.toLowerCase().includes(term) || p.legajo.toLowerCase().includes(term)
        );
        
        this.personalList.innerHTML = filtered.map(p => `
            <div class="list-item">
                <div class="item-info">
                    <h3>${p.grado} ${p.nombre}</h3>
                    <p>Legajo: ${p.legajo} | Unidad: ${p.unidad}</p>
                </div>
                <div class="item-actions">
                    <button class="hours" onclick="app.showHorasModal('${p.id}')"><i class="fas fa-clock"></i></button>
                    <button class="edit" onclick="app.showAddPersonalModal('${p.id}')"><i class="fas fa-edit"></i></button>
                    <button class="delete" onclick="app.deletePersonal('${p.id}')"><i class="fas fa-trash"></i></button>
                </div>
            </div>
        `).join('') || '<p class="text-center" style="color:var(--text-muted)">No hay personal registrado.</p>';
    }

    // --- UNIDADES MANAGEMENT ---
    
    showAddUnidadModal() {
        const nombre = prompt("Nombre de la nueva Unidad:");
        if (nombre && nombre.trim() !== '') {
            if(!this.data.unidades.includes(nombre.trim().toUpperCase())) {
                this.data.unidades.push(nombre.trim().toUpperCase());
                this.saveData();
                this.renderUnidades();
            }
        }
    }
    
    deleteUnidad(nombre) {
        if(confirm(`¿Eliminar la unidad ${nombre}?`)) {
            this.data.unidades = this.data.unidades.filter(u => u !== nombre);
            this.saveData();
            this.renderUnidades();
        }
    }

    renderUnidades() {
        this.unidadesList.innerHTML = this.data.unidades.map(u => `
            <div class="list-item">
                <div class="item-info">
                    <h3>${u}</h3>
                </div>
                <div class="item-actions">
                    <button class="delete" onclick="app.deleteUnidad('${u}')"><i class="fas fa-trash"></i></button>
                </div>
            </div>
        `).join('');
    }

    // --- HORAS MANAGEMENT ---

    showHorasModal(personalId) {
        this.currentPersonalId = personalId;
        const person = this.data.personal.find(p => p.id === personalId);
        document.getElementById('horas-personal-name').textContent = `${person.grado} ${person.nombre}`;
        
        // Default to today if empty, otherwise last entered date for flow
        let lastDateStr = new Date().toISOString().split('T')[0];
        const personHours = this.data.horas.filter(h => h.personalId === personalId);
        if(personHours.length > 0) {
            const sorted = personHours.sort((a,b) => new Date(b.fecha) - new Date(a.fecha));
            // Just suggest the day after the last entry for fluidity
            const nextDay = new Date(sorted[0].fecha);
            nextDay.setDate(nextDay.getDate() + 1);
            lastDateStr = nextDay.toISOString().split('T')[0];
        }
        
        document.getElementById('hora-fecha').value = lastDateStr;
        document.getElementById('hora-entrada').value = "08:00";
        document.getElementById('hora-salida').value = "08:00";
        
        this.currentDate = new Date();
        this.updateMonthView();
        
        this.modalHoras.classList.add('show');
    }

    changeMonth(delta) {
        this.currentDate.setMonth(this.currentDate.getMonth() + delta);
        this.updateMonthView();
    }

    updateMonthView() {
        const year = this.currentDate.getFullYear();
        const month = String(this.currentDate.getMonth() + 1).padStart(2, '0');
        this.monthSelector.value = `${year}-${month}`;
        
        const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        this.monthDisplay.textContent = `${monthNames[this.currentDate.getMonth()]} ${year}`;
        
        this.renderHoras();
    }

    handleAddHora(e) {
        e.preventDefault();
        const fecha = document.getElementById('hora-fecha').value;
        const entrada = document.getElementById('hora-entrada').value;
        const salida = document.getElementById('hora-salida').value;
        
        if(!fecha || !entrada || !salida) return;

        let entParts = entrada.split(':');
        let salParts = salida.split(':');
        
        let entMins = parseInt(entParts[0])*60 + parseInt(entParts[1]);
        let salMins = parseInt(salParts[0])*60 + parseInt(salParts[1]);
        
        let diffMins = salMins - entMins;
        // Si salida <= entrada, asumimos que pasa al día siguiente
        if (diffMins <= 0) {
            diffMins += 24 * 60;
        }
        
        const horasCalculadas = diffMins / 60;

        const newRecord = {
            id: Date.now().toString(),
            personalId: this.currentPersonalId,
            fecha, // YYYY-MM-DD
            entrada,
            salida,
            horasCalculadas
        };

        this.data.horas.push(newRecord);
        this.saveData();
        
        // Fluidity: advance date by 1 for the next entry
        const d = new Date(fecha);
        d.setDate(d.getDate() + 2); // Jump 2 days usually for guards? Let's just keep the last entered
        // Actually, just keep it, or clear it. We'll leave it to let user change.
        
        // Update view to the month of the entered date
        this.currentDate = new Date(fecha + "T00:00:00");
        this.updateMonthView();
    }

    deleteHora(id) {
        this.data.horas = this.data.horas.filter(h => h.id !== id);
        this.saveData();
        this.renderHoras();
    }

    renderHoras() {
        if (!this.currentPersonalId) return;

        const year = this.currentDate.getFullYear();
        const month = String(this.currentDate.getMonth() + 1).padStart(2, '0');
        const prefix = `${year}-${month}`;

        const personHours = this.data.horas.filter(h => h.personalId === this.currentPersonalId);
        
        const monthHours = personHours.filter(h => h.fecha.startsWith(prefix));
        // Sort by date ascending
        monthHours.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));

        this.horasList.innerHTML = monthHours.map(h => {
            const parts = h.fecha.split('-');
            const displayDate = `${parts[2]}/${parts[1]}/${parts[0]}`;
            return `
            <div class="mini-list-item">
                <span><strong>${displayDate}</strong>: ${h.entrada} a ${h.salida} (${h.horasCalculadas} hs)</span>
                <button class="delete-hora" onclick="app.deleteHora('${h.id}')"><i class="fas fa-times"></i></button>
            </div>
            `;
        }).join('') || '<p style="font-size:0.85rem; color:#94a3b8">No hay registros este mes.</p>';

        // Calculations
        const totalMonth = monthHours.reduce((acc, curr) => acc + curr.horasCalculadas, 0);
        
        const yearHours = personHours.filter(h => h.fecha.startsWith(`${year}-`));
        const totalYear = yearHours.reduce((acc, curr) => acc + curr.horasCalculadas, 0);

        const promedioSemanal = totalYear / 52;
        const excedente = promedioSemanal - 35;
        let diasCompensatoria = 0;
        
        if (excedente > 0) {
            diasCompensatoria = Math.round(excedente);
            if (diasCompensatoria > 15) diasCompensatoria = 15;
        }

        document.getElementById('summary-month-hours').textContent = totalMonth.toFixed(1);
        document.getElementById('summary-year-hours').textContent = totalYear.toFixed(1);
        document.getElementById('summary-compensatoria').textContent = diasCompensatoria;
    }

    // --- EXPORT / IMPORT ---

    exportData() {
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.data));
        const downloadAnchorNode = document.createElement('a');
        downloadAnchorNode.setAttribute("href",     dataStr);
        downloadAnchorNode.setAttribute("download", "sumahoras_backup.json");
        document.body.appendChild(downloadAnchorNode);
        downloadAnchorNode.click();
        downloadAnchorNode.remove();
    }

    importData(e) {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const json = JSON.parse(e.target.result);
                if (json.personal && json.unidades && json.horas) {
                    this.data = json;
                    this.saveData();
                    this.init();
                    this.modalSync.classList.remove('show');
                    alert("Datos importados correctamente.");
                } else {
                    alert("Formato de archivo inválido.");
                }
            } catch (err) {
                alert("Error al leer el archivo.");
            }
        };
        reader.readAsText(file);
    }

    // --- PDF GENERATION ---
    generatePDF() {
        if (!this.currentPersonalId) return;
        
        const person = this.data.personal.find(p => p.id === this.currentPersonalId);
        const year = this.currentDate.getFullYear();
        const month = String(this.currentDate.getMonth() + 1).padStart(2, '0');
        const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        const monthName = monthNames[this.currentDate.getMonth()];

        const personHours = this.data.horas.filter(h => h.personalId === this.currentPersonalId);
        const monthHoursList = personHours.filter(h => h.fecha.startsWith(`${year}-${month}`));
        monthHoursList.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));

        const yearHoursList = personHours.filter(h => h.fecha.startsWith(`${year}-`));
        const totalYear = yearHoursList.reduce((acc, curr) => acc + curr.horasCalculadas, 0);
        
        const promedioSemanal = totalYear / 52;
        const excedente = promedioSemanal - 35;
        let diasCompensatoria = 0;
        if (excedente > 0) {
            diasCompensatoria = Math.round(excedente);
            if (diasCompensatoria > 15) diasCompensatoria = 15;
        }

        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        
        doc.setFontSize(18);
        doc.text("Planilla de Control de Horas de Servicio", 14, 20);
        
        doc.setFontSize(12);
        doc.text(`Personal: ${person.grado} ${person.nombre} (Legajo: ${person.legajo})`, 14, 30);
        doc.text(`Unidad de Revista: ${person.unidad}`, 14, 37);
        doc.text(`Período: ${monthName} ${year}`, 14, 44);

        // Tabla del mes
        const tableData = monthHoursList.map(h => {
            const parts = h.fecha.split('-');
            return [
                `${parts[2]}/${parts[1]}/${parts[0]}`, 
                h.entrada, 
                h.salida, 
                h.horasCalculadas.toString()
            ];
        });

        doc.autoTable({
            startY: 50,
            head: [['Fecha', 'Entrada', 'Salida', 'Horas Computadas']],
            body: tableData,
            theme: 'grid',
            headStyles: { fillColor: [59, 130, 246] }
        });

        let finalY = doc.lastAutoTable.finalY || 50;

        const totalMonth = monthHoursList.reduce((acc, curr) => acc + curr.horasCalculadas, 0);
        doc.setFontSize(11);
        doc.text(`Total Horas Mensuales: ${totalMonth.toFixed(1)} hs`, 14, finalY + 10);
        
        doc.setFontSize(14);
        doc.text(`Resumen Anual (${year})`, 14, finalY + 25);
        
        doc.setFontSize(11);
        doc.text(`Total Horas Anuales Acumuladas: ${totalYear.toFixed(1)} hs`, 14, finalY + 35);
        doc.text(`Promedio Semanal: ${promedioSemanal.toFixed(2)} hs`, 14, finalY + 42);
        
        let excText = excedente > 0 ? excedente.toFixed(2) : "0";
        doc.text(`Excedente Promedio: ${excText} hs`, 14, finalY + 49);
        
        doc.setFontSize(12);
        doc.setFont("helvetica", "bold");
        doc.text(`Licencia Compensatoria (Días): ${diasCompensatoria}`, 14, finalY + 58);

        // Footer Branding
        doc.setFontSize(9);
        doc.setFont("helvetica", "italic");
        doc.setTextColor(150, 150, 150);
        doc.text("Software creado por Argos-Dev", 14, 285);

        doc.save(`Horas_${person.legajo}_${monthName}_${year}.pdf`);
    }
}

// Initialize App
const app = new App();

// Register Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .then(reg => console.log('Service Worker registrado', reg))
      .catch(err => console.error('Error al registrar SW', err));
  });
}
