CREATE DATABASE IF NOT EXISTS `sample01`;
USE sample01;
CREATE TABLE IF NOT EXISTS `users`
(
 `id`               INT(20) AUTO_INCREMENT,
 `name`             VARCHAR(50) NOT NULL,
 `password`         VARCHAR(150) NOT NULL,
 `email`            VARCHAR(50) NOT NULL,
 `role_id`          int(2) NOT NULL,
 `salt`             VARCHAR(100) NOT NULL DEFAULT "koR54sfR472wsdr0ol5TYdGhEfcm",
 `created_at`       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE IF NOT EXISTS `roles`
(
 `id`               INT(20) AUTO_INCREMENT,
 `name`             VARCHAR(50) NOT NULL,
 `created_at`       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO users (name, password, email, role_id) VALUES ("織田信長", "734d2fb94daa6045bbf2df929a14093b3b0a3183fe0af12c5f19ec58268efbbafd06b4edeba2fdcaf07bdbcf17c6717fe3bbe126875a0fe0340b4a5865205465", "oda@test.com", 1);
INSERT INTO users (name, password, email, role_id) VALUES ("羽柴秀吉", "0c1cb792ce387dec41cb43dd28ea71e3edbbcd6f03580e3eb52552770d5200e0be73d5c456ccf205e65a17977318307d4f1c604a93f3ca040ad1137b2aa73645", "hashiba@test.com", 1);
INSERT INTO users (name, password, email, role_id) VALUES ("竹中半兵衛", "c36d777ea96ff319cd490fa3f9b35180442b612e19c28a4f9d8f352a0a7d48d308093806c5f7b2d0e7ae3273f29d6a8d73736d6e78499c07bf04fda8590aad28", "takenaka@test.com", 2);
INSERT INTO users (name, password, email, role_id) VALUES ("徳川家康", "dddba2dc1107564bc5d04073ba7e3c0ec40d2a78f1d887141d7feb9a05f9a170564741f15d165eaebc84bbe5e929887bdc84a429075bb50022e645047a3e8e2c", "tokugawa@test.com", 1);
INSERT INTO users (name, password, email, role_id) VALUES ("本多忠勝", "19e83c1e120a8f0200fa6041d9c371520de5a6cb53a66a5257ae44701fa5e5639a10eee784887470ecfdf00b20c110e8151caddcd7d87688af1257ca597d5d41", "honda@test.com", 3);

INSERT INTO roles (id, name) VALUES (1, "大名");
INSERT INTO roles (id, name) VALUES (2, "軍師");
INSERT INTO roles (id, name) VALUES (3, "武将");
