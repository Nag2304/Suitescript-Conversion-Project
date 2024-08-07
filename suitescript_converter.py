import re

conversion_patterns = [
    # Record manipulation
    (r"nlapiLoadRecord\s*\(\s*'(\w+)'\s*,\s*(\w+)\s*\)", r"record.load({type:'\1',id:\2})"),
    (r"nlapiCreateRecord\s*\(\s*'(\w+)'\s*\)", r"record.create({type:'\1'})"),
    (r"nlapiSubmitRecord\s*\(\s*(\w+)\s*\)", r"\1.save()"),
    (r"nlapiDeleteRecord\s*\(\s*'(\w+)'\s*,\s*(\w+)\s*\)", r"record.delete({type:'\1',id:\2})"),

    # Field manipulation
    (r"nlapiGetFieldValue\s*\(\s*'(\w+)'\s*\)", r"record.getValue({fieldId:'\1'})"),
    (r"nlapiSetFieldValue\s*\(\s*'(\w+)'\s*,\s*'(.+?)'\s*\)", r"record.setValue({fieldId:'\1', value:'\2'})"),
    (r"nlapiGetFieldText\s*\(\s*'(\w+)'\s*\)", r"record.getText({fieldId:'\1'})"),
    (r"nlapiSetFieldText\s*\(\s*'(\w+)'\s*,\s*'(.+?)'\s*\)", r"record.setText({fieldId:'\1', text:'\2'})"),

    # Sublist manipulation
    (r"nlapiGetLineItemValue\s*\(\s*'(\w+)'\s*,\s*'(\w+)'\s*,\s*(\d+)\s*\)",
     r"record.getSublistValue({sublistId:'\1', fieldId:'\2', line:\3})"),
    (r"nlapiSetLineItemValue\s*\(\s*'(\w+)'\s*,\s*'(\w+)'\s*,\s*(\d+)\s*,\s*'(.+?)'\s*\)",
     r"record.setSublistValue({sublistId:'\1', fieldId:'\2', line:\3, value:'\4'})"),
    (r"nlapiInsertLineItem\s*\(\s*'(\w+)'\s*,\s*(\d+)\s*\)", r"record.insertLine({sublistId:'\1', line:\2})"),
    (r"nlapiRemoveLineItem\s*\(\s*'(\w+)'\s*,\s*(\d+)\s*\)", r"record.removeLine({sublistId:'\1', line:\2})"),

    # Search functions
    (r"nlapiSearchRecord\s*\(\s*'(\w+)'\s*,\s*'(\w+)'\s*,\s*(\[.*?\])\s*,\s*(\[.*?\])\s*\)",
     r"search.create({type:'\1', filters:\3, columns:\4}).run().getRange({start: 0, end: 1000})"),
    (r"nlapiSearchRecord\s*\(\s*'(\w+)'\s*,\s*(null)\s*,\s*(\[.*?\])\s*\)",
     r"search.create({type:'\1', filters:\3}).run().getRange({start: 0, end: 1000})"),
    (r"nlapiSearchRecord\s*\(\s*'(\w+)'\s*,\s*(null)\s*\)",
     r"search.create({type:'\1'}).run().getRange({start: 0, end: 1000})"),

    # Record references
    (r"nlapiCopyRecord\s*\(\s*'(\w+)'\s*,\s*(\w+)\s*\)", r"record.copy({type:'\1', id:\2})"),

    # Logging
    (r"nlapiLogExecution\s*\(\s*'(\w+)'\s*,\s*'(.+?)'\s*,\s*(.+?)\s*\)", r"log.\1({title:'\2', details:\3})"),

    # Utilities
    (r"nlapiLookupField\s*\(\s*'(\w+)'\s*,\s*(\w+)\s*,\s*'(\w+)'\s*\)",
     r"search.lookupFields({type:'\1', id:\2, columns:['\3']})['\3']"),
    (r"nlapiLookupField\s*\(\s*'(\w+)'\s*,\s*(\w+)\s*,\s*(\[.*?\])\s*\)",
     r"search.lookupFields({type:'\1', id:\2, columns:\3})"),
    (
    r"nlapiSendEmail\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*'(.+?)'\s*,\s*'(.+?)'\s*,\s*(\[.*?\])?\s*,\s*(\[.*?\])?\s*,\s*(\w+)?\s*,\s*(.+?)?\s*\)",
    r"email.send({author:\1, recipients:\2, subject:'\3', body:'\4', cc:\5, bcc:\6, replyTo:\7, attachments:\8})"),
    (r"nlapiFormatDate\s*\(\s*(.+?)\s*\)", r"format.format({value:\1, type:format.Type.DATE})"),
    (r"nlapiFormatCurrency\s*\(\s*(.+?)\s*\)", r"format.format({value:\1, type:format.Type.CURRENCY})"),
]


def convert_suitescript(script):
    for pattern, replacement in conversion_patterns:
        script = re.sub(pattern, replacement, script)
    return script
