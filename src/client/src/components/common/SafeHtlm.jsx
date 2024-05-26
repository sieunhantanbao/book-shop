import React from 'react';
import DOMPurify from 'dompurify';

function SafeHtlm({ rawHtlm }) {
    const safeHTML = DOMPurify.sanitize(rawHtlm);
    return (
        <div dangerouslySetInnerHTML={{ __html: safeHTML }} />
    );
}
export default SafeHtlm;
