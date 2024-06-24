function transform(line) {
    var values = line.split(",");
    const obj = {
        "Invoice_ID": values[0],
        "Branch": values[1],
        "City": values[2],
        "Customer_type": values[3],
        "Gender": values[4],
        "Product_line": values[5],
        "Unit_price": parseFloat(values[6]),
        "Quantity": parseInt(values[7], 10),
        "Tax_5": parseFloat(values[8]),
        "Total": parseFloat(values[9]),
        "Date": values[10],
        "Time": values[11],
        "Payment": values[12],
        "cogs": parseFloat(values[13]),
        "gross_margin_percentage": parseFloat(values[14]),
        "gross_income": parseFloat(values[15]),
        "Rating": parseFloat(values[16])
    };
    return JSON.stringify(obj);
}
