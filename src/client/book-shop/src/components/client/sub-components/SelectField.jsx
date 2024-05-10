import React from 'react';

function SelectField({ name, value, onChange, options }) {
    return (
            <select
                className="form-select form-select-sm"
                name={name}
                value={value}
                onChange={onChange}
            >
                {options.map(option => (
                    <option key={option.value} value={option.value}>{option.label}</option>
                ))}
            </select>
    );
}

export default SelectField;