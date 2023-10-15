-- AlterTable
ALTER TABLE "users" ADD COLUMN     "verification_code" VARCHAR(255);

-- CreateTable
CREATE TABLE "routes" (
    "id" SERIAL NOT NULL,
    "start_location" VARCHAR(255) NOT NULL,
    "end_location" VARCHAR(255) NOT NULL,
    "price_per_km" DOUBLE PRECISION NOT NULL,
    "distance" DOUBLE PRECISION NOT NULL,
    "date_of_execution" DATE NOT NULL,

    CONSTRAINT "routes_pkey" PRIMARY KEY ("id")
);
