# تعریف jobها
jobs = [
    {'id': 'J1', 'deadline': 2, 'profit': 40},
    {'id': 'J2', 'deadline': 1, 'profit': 50},
    {'id': 'J3', 'deadline': 4, 'profit': 30},
    {'id': 'J4', 'deadline': 2, 'profit': 100}
]

# مرتب‌سازی بر اساس profit به صورت نزولی
jobs.sort(key=lambda x: x['profit'], reverse=True)

# پیدا کردن dmax
dmax = max(job['deadline'] for job in jobs)

# لیست زمان‌بندی (index از 1 تا dmax) و مقداردهی اولیه
ts = [None] * (dmax + 1)  # ts[0] استفاده نمی‌شه

# مجموع سود
total_profit = 0

# الگوریتم طبق pseudo-code
for i in range(len(jobs)):
    job = jobs[i]
    k = min(dmax, job['deadline'])
    
    while k >= 1:
        if ts[k] is None:
            ts[k] = job['id']
            total_profit += job['profit']
            break
        k -= 1

# چاپ زمان‌بندی نهایی
print("Job Schedule (Tabu Style):")
for t in range(1, dmax + 1):
    print(f"Time {t}: {ts[t]}")

print(f"\nMaximum Profit: {total_profit}")
