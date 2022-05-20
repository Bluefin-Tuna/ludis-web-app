import React from 'react';

import './Modal.component.css';
import iconX from '../iconmonstr-x-mark-1.svg';

interface ModalProps {
  title: string;
  isOpen: boolean;
  onClose: () => void;
}

export const Modal: React.FC<ModalProps> = ({ title, isOpen, onClose, children }) => {
  const outsideRef = React.useRef(null);

  const handleCloseOnOverlay = (e: React.MouseEvent<HTMLElement, MouseEvent>) => {
    if (e.target === outsideRef.current) {
      onClose();
    }
  }

  return isOpen ? (
    <div className={'modal'}>
      <div
        ref={outsideRef}
        className={'modal__overlay'}
        onClick={handleCloseOnOverlay}
      />
      <div className={'modal__box'}>
        <button
          className={'modal__close'}
          onClick={onClose}
          style={{ background: 'transparent', border: 0 }}
        >
          <img src={iconX} alt={'close'} />
        </button>
        <div className={'modal__title'}>
          {title}
        </div>
        <div className={'modal__content'}>
          {children}
        </div>
      </div>
    </div>
  ) : null;
};