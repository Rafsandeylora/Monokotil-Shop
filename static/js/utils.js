// static/js/utils.js
function showToast(message, type) {
    const toastContainer = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `p-4 mb-3 rounded-lg shadow-md transition-transform duration-300 translate-x-full ease-out`;

    if (type === 'success') {
        toast.classList.add('bg-green-100', 'text-green-800');
    } else if (type === 'error') {
        toast.classList.add('bg-red-100', 'text-red-800');
    }

    toast.textContent = message;
    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.classList.remove('translate-x-full');
        toast.classList.add('translate-x-0');
    }, 10);

    setTimeout(() => {
        toast.classList.remove('translate-x-0');
        toast.classList.add('translate-x-full');
        toast.addEventListener('transitionend', () => toast.remove());
    }, 3000);
}

function showModal(modalId) {
    const modal = document.getElementById(modalId);
    const backdrop = document.getElementById('modal-backdrop');
    backdrop.classList.remove('hidden', 'opacity-0');
    backdrop.classList.add('opacity-100');
    modal.classList.remove('hidden', 'scale-95', 'opacity-0');
    modal.classList.add('scale-100', 'opacity-100');
}

function hideModal(modalId) {
    const modal = document.getElementById(modalId);
    const backdrop = document.getElementById('modal-backdrop');
    modal.classList.remove('scale-100', 'opacity-100');
    modal.classList.add('scale-95', 'opacity-0');
    backdrop.classList.remove('opacity-100');
    backdrop.classList.add('opacity-0');
    modal.addEventListener('transitionend', () => {
        modal.classList.add('hidden');
        backdrop.classList.add('hidden');
    }, { once: true });
}