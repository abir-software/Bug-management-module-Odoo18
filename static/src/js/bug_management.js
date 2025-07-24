odoo.define('bug_management.bug_management', function (require) {
    "use strict";
    
    var ListRenderer = require('web.ListRenderer');
    
    ListRenderer.include({
        _renderHeaderCell: function (node) {
            var $th = this._super.apply(this, arguments);
            if (node.attrs.name === 'severity') {
                $th.addClass('text-center');
            }
            return $th;
        },
        
        _renderBodyCell: function (record, node, colIndex, options) {
            var $td = this._super.apply(this, arguments);
            if (node.attrs.name === 'severity') {
                $td.addClass('text-center o_bug_severity_' + record.data.severity);
            }
            return $td;
        },
    });
});