#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Compile: gcc chall.c -o chall -no-pie -fstack-protector

int inventory[3] = {0};

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void init2(){
    asm("xchg %rdi, %rax; ret");
    asm("pop %rax; ret");
}

void barang_tersembunyi(int passKey){
    FILE *file;
    char flag[64];

    if (passKey == 0x12345678){
        file = fopen("flag.txt", "r");
        if (file == NULL){
            printf("Eh mana ya barangnya?\n");
            return;
        }

        while (fgets(flag, sizeof(flag), file)){
            printf("Ini buat kamu aja deh barang tersembunyinya.\n%s\n", flag);
            exit(1);
        }
    } else {
        printf("???\n");
    }
}

void beli_barang(int pilihanUser, int *saldoUser, int *quantity){
    int price[3] = {10000, 18000, 25000};
    printf("Berapa jumlah barang yang ingin dibeli? ");
    scanf(" %ld", quantity); getchar();

    int total = *quantity * price[pilihanUser];
    if (total > 0 && total <= *saldoUser){
        *saldoUser -= total;
        inventory[pilihanUser] += *quantity;
        printf("Pembelian berhasil. Sisa saldo: %d\n\n", *saldoUser);
    } else if (total <= 0) {
        printf("Pembelian tidak valid.\n\n");
    } else {
        printf("Saldo kamu tidak cukup.\n\n");
    }
}

void display_barang(int *saldoUser, int *quantity){
    printf("Berikut barang-barang yang tersedia:\n");
    printf("1. Kartu Ucapan - Rp10000,00\n");
    printf("2. Coklat IndoApril - Rp18000,00\n");
    printf("3. Mainan Mobil - Rp25000,00\n");
    printf("Apakah anda ingin membeli sesuatu (Y\\N)? ");

    char pilihanUser;
    scanf(" %c", &pilihanUser); getchar();

    if (pilihanUser == 'Y' || pilihanUser == 'y'){
        printf("Barang apa yang ingin anda beli (1-3)? ");
        int pilihanBarang;
        scanf(" %d", &pilihanBarang); getchar();
        
        if (pilihanBarang >= 1 && pilihanBarang <= 3){
            beli_barang(pilihanBarang-1, saldoUser, quantity);
        } else puts("");
    } else puts("");
}

int display_inv_status(int printInv){
    int i, empty = 1;
    for (i = 0; i < 3; i++){
        if (inventory[i] > 0){
            empty = 0;
            if (printInv){
                if (i == 0){
                    printf("[%d] Kartu Ucapan: %d pcs\n", i+1, inventory[i]);
                } else if (i == 1){
                    printf("[%d] Coklat IndoApril: %d pcs\n", i+1, inventory[i]);
                } else {
                    printf("[%d] Mainan Mobil: %d pcs\n", i+1, inventory[i]);
                }
            }
        }
    }

    if (empty){
        puts("Tidak ada barang untuk saat ini.\n");
    }

    return empty;
}

void display_inventory(int *sizeKartu){
    char pilihanUser = 'Y';
    char kartuUcapan[64];

    while ((pilihanUser == 'Y' || pilihanUser == 'y') && !display_inv_status(1)){
        printf("Apakah kamu ingin menggunakan barang yang telah dibeli (Y\\N)? ");
        scanf(" %c", &pilihanUser); getchar();

        int pilihanBarang;
        if (pilihanUser == 'Y' || pilihanUser == 'y'){
            printf("Barang apa yang ingin anda gunakan (1-3)? ");
            scanf(" %d", &pilihanBarang); getchar();

            if (pilihanBarang > 0 && pilihanBarang <= 3 && inventory[pilihanBarang-1] > 0){
                char kartuUcapan[64];
                if (*sizeKartu == 0) *sizeKartu = 64;
                // printf("Size kartu: %d\n", *sizeKartu);

                if (pilihanBarang == 1){
                    puts("Kamu menulis di kartu ucapan...\n");
                    puts("Apa yang ingin kamu ucapkan?");
                    // fgets(kartuUcapan, *sizeKartu, stdin);
                    read(0, kartuUcapan, *sizeKartu - 1);
                    printf("Kamu mengucapkan:\n%s\n", kartuUcapan);
                } else if (pilihanBarang == 2){
                    puts("Kamu memakan coklatnya...\n");
                } else {
                    puts("Kamu tidak sengaja merusak mainannya...\n");
                }
                inventory[pilihanBarang-1]--;
            } else puts("");
        } else puts("");
    }
}

void display_saldo(int *saldoUser){
    printf("Saldo anda saat ini: Rp%d,00\n\n", *saldoUser);
}

int store(){
    int quantity = 0;
    int sizeKartu = 64;
    int pilihanUser;
    int saldoUser = 21000;

    puts("Halo! Selamat datang di Chrono Bazaar.");
    puts("Silakan melihat-lihat barang yang kami jual :D\n");

    while (1){
        // printf("Size kartu: %d\n", sizeKartu);
        puts("1. Cek barang yang tersedia.");
        puts("2. Cek barang yang sudah dibeli.");
        puts("3. Cek saldo yang dimiliki.");
        puts("4. Keluar.");
        printf("> ");

        scanf(" %d", &pilihanUser); getchar();
        if (pilihanUser == 1){
            display_barang(&saldoUser, &quantity);
        } else if (pilihanUser == 2){
            display_inventory(&sizeKartu);
        } else if (pilihanUser == 3){
            display_saldo(&saldoUser);
        } else {
            break;
        }
    }

    puts("Terima kasih sudah berbelanja dan selamat datang kembali!");
}

int main(){
    init();
    store();

    return 0;
}