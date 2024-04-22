/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { AccountReportFilters } from "@account_reports/components/account_report/filters/filters";
import { useState } from "@odoo/owl";

patch(AccountReportFilters.prototype, {
    setup() {
        super.setup();
        this.selectedItems = useState([]);
    },
    async customFilter(filter) {

        if (this.selectedItems.includes(filter.id)){
            const index = this.selectedItems.indexOf(filter.id);
            this.selectedItems.splice(index, 1);
        } else {
            this.selectedItems.push(filter.id);
        }

        const journalFilter = this.controller.options.journals.filter((journal)=> journal.account_journal_type === filter.id);

        for (var journal of journalFilter){
            journal.selected = !journal.selected;
        }
        filter.is_selected = !filter.is_selected;
        await this.controller.reload('journals', this.controller.options);
    }
});