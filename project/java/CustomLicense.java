package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A license that is not listed on the SPDX License List.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CustomLicense extends License {



}